# -*- coding: utf-8 -*-
from visual import *
from visual.graph import *

G = 6.67 
m = 10 #mass
L = 10 #each ball's distance to each others

v = (G*m/L)**0.5 #速度的純量

def Fg(x): #定義萬有引力函數, parameter: distance
    return -G*m*m/(x**2)
 
scene = display(width=900, height=600, center=(0,0,0),
                background=(8.0/255,8.0/255,8.0/255),range=2*L)

text(text='Yee', align='center', depth=1, material=materials.earth, pos = vector(0,0,0)) #Yee.

ball1_pos = vector(-L / 2, -L / (3**0.5 * 2), 0) #左下
ball2_pos = vector( L / 2, -L / (3**0.5 * 2), 0) #右下
ball3_pos = vector(   0  ,  L / (3**0.5)    , 0) #中上

ball1 = sphere(pos=ball1_pos, radius=1, make_trail=true, retain=4444, material=materials.earth, color=color.blue)
ball2 = sphere(pos=ball2_pos, radius=1, make_trail=true, retain=4444, material=materials.earth, color=color.yellow)
ball3 = sphere(pos=ball3_pos, radius=1, make_trail=true, retain=4444, material=materials.earth, color=color.red)

ball1.v = vector(-v*cos(pi/3), v*sin(pi/3), 0)
ball2.v = vector(-v*cos(pi/3), -v*sin(pi/3), 0)
ball3.v = vector(v, 0, 0)

def Calc_Spd_2d(NO): #para: ballNo.
    ball_v = [0, ball1.v, ball2.v, ball3.v]
    return (ball_v[NO].x**2 + ball_v[NO].y**2)**0.5

t = 0 ; dt = 0.001

while True:
    rate(2017)
    # 將純量改為向量
    dist12 = ((ball1.x-ball2.x)**2+(ball1.y-ball2.y)**2+(ball1.z-ball2.z)**2)**0.5
    radiavector12 = (ball2.pos-ball1.pos)/dist12
    Fg_vector12 = Fg(dist12)*radiavector12 #行星所受萬有引力

    ball1.v += -Fg_vector12/m*dt #ball1受力 力生加速度, 產生速度變化 
    ball2.v += Fg_vector12/m*dt #ball2受力 力生加速度, 產生速度變化
    

    dist23 = ((ball2.x-ball3.x)**2+(ball2.y-ball3.y)**2+(ball2.z-ball3.z)**2)**0.5
    radiavector23 = (ball3.pos-ball2.pos)/dist23
    Fg_vector23 = Fg(dist23)*radiavector23 #行星所受萬有引力

    ball2.v += -Fg_vector23/m*dt #ball1受力 力生加速度, 產生速度變化 
    ball3.v += Fg_vector23/m*dt #ball2受力 力生加速度, 產生速度變化


    dist31 = ((ball3.x-ball1.x)**2+(ball3.y-ball1.y)**2+(ball3.z-ball1.z)**2)**0.5
    radiavector31 = (ball1.pos-ball3.pos)/dist31
    Fg_vector31 = Fg(dist31)*radiavector31 #行星所受萬有引力

    ball3.v += -Fg_vector31/m*dt #ball1受力 力生加速度, 產生速度變化 
    ball1.v += Fg_vector31/m*dt #ball2受力 力生加速度, 產生速度變化


    ball1.pos = ball1.pos + ball1.v*dt #ball1開始運動 速度產生位置變化
    ball2.pos = ball2.pos + ball2.v*dt #ball2開始運動 速度產生位置變化
    ball3.pos = ball3.pos + ball3.v*dt #ball3開始運動 速度產生位置變化

    if t % 1 >= 0.999: 
        print "t=", t, ": v="
        print Calc_Spd_2d(1), " / ", Calc_Spd_2d(2), " / ", Calc_Spd_2d(3)
  
    t = t+dt