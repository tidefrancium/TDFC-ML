import math
import torch
from torch.optim.optimizer import Optimizer

class AdamT(Optimizer):
    """
    Copyright (c) 2025 Xu Minghao
    新发明——AdamT优化器 - 引入余弦退火机制的Adam变种
    原作者：徐铭浩 University of Science and Technology Beijing
    参数:
        params (iterable): 待优化的参数迭代器,和Adam无本质区别
        lr (float, optional): 基础学习率 (默认: 0.001),和Adam无本质区别
        betas (Tuple[float, float], optional): 用于计算梯度及其平方的运行平均值的系数 (默认范围: (0.9, 0.999))类似余弦退火
        eps (float, optional): 增加数值稳定性的小常数 (默认: 1e-8)只是为了保险
        weight_decay (float, optional): 权重衰减系数 (默认: 0)新增功能
        T_max (int, optional): 温度调度的最大迭代次数 (默认: 1000)类似余弦退火，越小越容易收敛，但是不一定稳定
        eta_min (float, optional): 温度的最小值 (默认: 0.1)类似余弦退火
        temperature_init (float, optional): 初始温度 (默认: 1.0)
    """
    
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8,
                 weight_decay=0, T_max=1000, eta_min=0.1, temperature_init=1.0):
        if not 0.0 <= lr:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if not 0.0 <= eps:
            raise ValueError("Invalid epsilon value: {}".format(eps))
        if not 0.0 <= betas[0] < 1.0:
            raise ValueError("Invalid beta parameter at index 0: {}".format(betas[0]))
        if not 0.0 <= betas[1] < 1.0:
            raise ValueError("Invalid beta parameter at index 1: {}".format(betas[1]))
        if not 0.0 <= weight_decay:
            raise ValueError("Invalid weight_decay value: {}".format(weight_decay))
        if not 0.0 <= temperature_init:
            raise ValueError("Invalid initial temperature: {}".format(temperature_init))
        if not 0.0 <= eta_min <= temperature_init:
            raise ValueError("Invalid eta_min value: {} (must be <= temperature_init {})".format(eta_min, temperature_init))
        if not 1 <= T_max:
            raise ValueError("Invalid T_max value: {}".format(T_max))
        
        # 定义温度调度的参数
        defaults = dict(lr=lr, betas=betas, eps=eps,
                        weight_decay=weight_decay,
                        T_max=T_max, eta_min=eta_min,
                        temperature_init=temperature_init)
        super(AdamT, self).__init__(params, defaults)
        
        # 初始化迭代计数器
        for group in self.param_groups:
            group.setdefault('step', 0)

    def __setstate__(self, state):
        super(AdamT, self).__setstate__(state)
        for group in self.param_groups:
            group.setdefault('amsgrad', False)

    @torch.no_grad()
    def step(self, closure=None):
        """执行单步优化"""
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            params_with_grad = []
            grads = []
            exp_avgs = []
            exp_avg_sqs = []
            state_steps = []
            beta1, beta2 = group['betas']
            
            # 获取当前迭代步数
            group['step'] += 1
            step = group['step']
            
            # 计算当前温度 (余弦退火)
            temperature = group['eta_min'] + (group['temperature_init'] - group['eta_min']) * (
                1 + math.cos(math.pi * step / group['T_max'])) / 2
            
            # 计算温度调整后的学习率
            lr_t = group['lr'] * temperature
            
            # 计算温度调整后的beta1 (动量系数)
            # 温度高时(初期)动量小，允许快速探索；温度低时(后期)动量大，稳定收敛
            beta1_t = beta1 + (1 - beta1) * (1 - temperature)
            
            for p in group['params']:
                if p.grad is None:
                    continue
                params_with_grad.append(p)
                if p.grad.is_sparse:
                    raise RuntimeError('AdamT does not support sparse gradients')
                grads.append(p.grad)

                state = self.state[p]
                # 初始化状态
                if len(state) == 0:
                    state['step'] = 0
                    # 梯度的移动平均 (一阶矩)
                    state['exp_avg'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                    # 梯度平方的移动平均 (二阶矩)
                    state['exp_avg_sq'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                
                exp_avgs.append(state['exp_avg'])
                exp_avg_sqs.append(state['exp_avg_sq'])
                
                # 记录当前参数的迭代步数
                state['step'] = step
                state_steps.append(state['step'])

            # AdamT核心更新逻辑
            for i, param in enumerate(params_with_grad):
                grad = grads[i]
                exp_avg = exp_avgs[i]
                exp_avg_sq = exp_avg_sqs[i]
                step_t = state_steps[i]
                
                # 权重衰减 (AdamW方式)
                if group['weight_decay'] != 0:
                    grad = grad.add(param, alpha=group['weight_decay'])
                
                # 一阶矩和二阶矩更新
                exp_avg.mul_(beta1_t).add_(grad, alpha=1 - beta1_t)
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1 - beta2)
                
                # 计算偏差修正因子
                bias_correction1 = 1 - beta1_t ** step_t
                bias_correction2 = 1 - beta2 ** step_t
                
                # 计算修正后的学习率
                lr_t_adj = lr_t / bias_correction1
                
                # 计算分母 (二阶矩平方根 + epsilon)
                denom = (exp_avg_sq.sqrt() / math.sqrt(bias_correction2)).add_(group['eps'])
                
                # 执行参数更新
                param.addcdiv_(exp_avg, denom, value=-lr_t_adj)
                
        return loss