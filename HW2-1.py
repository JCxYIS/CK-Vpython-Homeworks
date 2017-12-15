from visual import *

g = 9.8             #重力加速度 9.8 m/s^2
size = 0.5          #球半徑 0.5 m
height = 15.0       #球初始高度 15 m
k = 0.1487630009487594878787878787000000800092000 #空阻係數,很糟

scene = display(width=600, height=600,x=0, y=0,
                center = (0,height/2,0), background=(0.5,0.5,0)) #設定畫面
floor = box(length=28, height=0.01, width=28, color=color.green)  #畫地板
ball = sphere(radius = size, color=color.yellow,
              make_trail= True, trail_type="points", interval=100) #畫球
Newball = sphere(radius = size, color=color.red,
              make_trail= True, trail_type="points", interval=100) #畫球球
Newtonball = sphere(radius = size, color=color.green,
              make_trail= True, trail_type="points", interval=100) #畫球球球

text(text='Yee', align='center', height= 7, depth=-0.93, color=color.green, pos = vector(0,4,0)) #Yee.


ball.pos = vector(0, size, 0)        #球初始位置       
ball.v = vector( 3, 18.763 , 0)              #球初速

Newball.pos = vector(0, size, 0)       #球初始位置       
Newball.v = vector( 3, 18.763 , 0)              #球初速

Newtonball.pos = vector(0, size, 0)
Newtonball.v = vector( 3, 18.763, 0)

dt = 0.001                              #時間間隔 0.001 秒
t = 0.0

while ball.pos.y >= 0 and Newball.pos.y >= 0 and Newtonball.pos.y >= 0: 
    rate(1000)                          #每一秒跑 1000 次

    t = t + dt    #timer
    
    ball.pos = ball.pos + ball.v * dt
    ball.v.y = ball.v.y - g*dt

    Newball.pos = Newball.pos + Newball.v * dt
    Newball.v.y = Newball.v.y - g*dt
    AirResistance = -k * Newball.v    #算空阻
    Newball.v += AirResistance * dt   #加空阻

    Newtonball.pos.x = Newtonball.v.x*(1-exp(-k*t))/k   #套公式
    Newtonball.pos.y = -g*t/k + (k*Newtonball.v.y+g)*(1-exp(-k*t))/k**2   #套公式

 

  

    


