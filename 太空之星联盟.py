import time
import sys

print("请输入船员编号")
a = int(input())
if(a > 10000):
   print("您是普通船员")
else:
   print("欢迎您，舰长")
print("舰员编号",a,"审核中……")
print("下面进行空间传输")
print("传送成功")
import random
print("为您分配飞船")
time.sleep(1)
fc = random.randint(1,10000)
print("分配成功，飞船编号为",fc,"正在进入轨道，请耐心等待……")
b = 5
while b >= 0:
   print(b)
   b -= 1
   time.sleep(0.5)

print("发射成功")
time.sleep(1)
print("开始新的旅程")
time.sleep(2)

xz = int(input("请选择飞行模式：1.安全模式 2.快速模式"))
print("您的选择为",xz)
time.sleep(2)
xl = 100
gj = 20
hj = 0
xlsx = 100
print("当前飞船血量：",xl,"当前飞船攻击：",gj,"当前飞船护甲",hj,"正在升级")
time.sleep(0.5)
while xz > 0:
   if xz == 1:
      xl += 50
      xz = 0
   else:
      gj += 5
      xz = 0

print("当前飞船血量：",xl,"当前飞船攻击：",gj,"当前飞船护甲",hj)
time.sleep(1)
print("前行中遇见敌方舰队")
dxl = 100
dgj = 10
while dxl > 0:
   if xl > 0:
      print("敌方剩余血量",dxl,"敌方目前攻击",dgj,"我方剩余血量",xl,"我方当前攻击",gj,"护甲",hj)
      print("1攻击 2修理")
      xz = int(input())
      if xz == 1:
         print("敌我互相攻击")
         dxl -= gj
         xl -= dgj - hj
      elif xz == 2:
          if xl < xlsx:
            print("飞船修复")
            xl += 20
            if xl > xlsx:
               xl = xlsx
            else:
               xl = xl
          else:
            print("飞船已经完全修复")
      else:
         print("别闹，按照游戏规则进行")
         print("敌方对你发动攻击")
         xl -= dgj - hj
   else:
      print("很遗憾，你死了")
      time.sleep(3)
      sys.exit()
print("恭喜您，刚刚打败了敌方飞船")
jl = random.randint(50,150)
jb = 0
jb += jl
print("你获得了",jl,"点金币")
print("当前金币为",jb,"打开商店中")
time.sleep(2)
print("老板：排队买最近装备啊，货不够，所有人限购一件！")
print("1究极护甲，2无敌炮台，3幸运赌博，各50金币，4不买")
sd = int(input())
if sd == 1 and jb >= 50:
   print("瞧瞧这装甲，越来越厚实")
   hj += 5
   jb -= 50
elif sd == 2 and jb >= 50:
   print("新的炮台威力就是强")
   gj += 5
   jb -= 50
elif sd == 3 and jb >= 50:
   jl = random.randint(10,90)
   print("你抽到了",jl,"金币")
   jb += jl
else:
   print("老板：你玩我不是，滚")
print("当前金币为：",jb,"准备进入下一次战斗")
time.sleep(2)
print("当前飞船血量：",xl,"当前飞船攻击：",gj,"护甲",hj)
time.sleep(1)
print("前行中遇见敌方新型舰队")
dxl = 200
dgj = 15
while dxl > 0:
   if xl > 0:
      print("敌方剩余血量",dxl,"敌方目前攻击",dgj,"我方剩余血量",xl,"我方当前攻击",gj,"护甲",hj)
      print("1攻击 2修理")
      xz = int(input())
      if xz == 1:
         print("敌我互相攻击")
         dxl -= gj
         xl -= dgj - hj
      elif xz == 2:
         
         if xl < xlsx:
            print("飞船修复")
            xl += 20
            if xl > xlsx:
               xl = xlsx
            else:
               xl = xl  
         else:
            print("飞船已经完全修复")
      else:
         print("别闹，按照游戏规则进行")
         print("敌方对你发动攻击")
         xl -= dgj - hj
   else:
      print("很遗憾，你死了")
      time.sleep(3)
      sys.exit()
print("恭喜您，刚刚打败了敌方飞船")
jl = random.randint(100,200)
jb += jl
print("你获得了",jl,"点金币")
print("当前金币为",jb,"打开商店中")
print("老板：排队买最近装备啊，货不够，所有人限购一件！")
print("1究极护甲，2无敌炮台，3幸运赌博，各50金币，4不买")
sd = int(input())
if sd == 1 and jb >= 50:
   print("瞧瞧这装甲，越来越厚实")
   hj += 5
   jb -= 50
elif sd == 2 and jb >= 50:
   print("新的炮台威力就是强")
   gj += 5
   jb -= 50
elif sd == 3 and jb >= 50:
   jl = random.randint(10,90)
   print("你抽到了",jl,"金币")
   jb += jl
else:
   print("老板：你玩我不是，滚")
print("当前金币为：",jb,"准备进入下一次战斗")
print("前行中遇见敌方航母舰队")
dxl = 500
dgj = 25
while dxl > 0:
   if xl > 0:
      print("敌方剩余血量",dxl,"敌方目前攻击",dgj,"我方剩余血量",xl,"我方当前攻击",gj,"护甲",hj)
      print("1攻击 2修理")
      xz = int(input())
      if xz == 1:
         print("敌我互相攻击")
         dxl -= gj
         xl -= dgj - hj
      elif xz == 2:
         
         if xl < xlsx:
            print("飞船修复")
            xl += 20
            if xl > xlsx:
               xl = xlsx
            else:
               xl = xl  
         else:
            print("飞船已经完全修复")
      else:
         print("别闹，按照游戏规则进行")
         print("敌方对你发动攻击")
         xl -= dgj - hj
   else:
      print("很遗憾，你死了")
      time.sleep(3)
      sys.exit()
print("恭喜您，刚刚打败了敌方舰队")
jl = random.randint(500,1000)
jb += jl
print("你获得了",jl,"点金币")
print("您已打败最终boss，太空之星恢复和平。")
time.sleep(5)