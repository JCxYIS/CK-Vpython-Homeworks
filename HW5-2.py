# -*- coding: utf-8 -*-
from visual import *
from visual.graph import *

G = 6.67 
m = 10 #mass
L = 10 #each ball's distance to each others

v = ( (2**1.5+1) * G*m / (4*(2**0.5 * L)) )**0.5 #速度!!!!

def Fg(x): #定義萬有引力函數, para: distance
    return -G*m*m/(x**2)
 
scene = display(width=600, height=600, center=(0,0,0),
                background=(8.0/255,8.0/255,8.0/255),range=2*L)

text(text='Yee', align='center', depth=1, material=materials.earth, pos = vector(0,0,0)) #Yee.

ball1_pos = vector(-L/2 , L/2 , 0) #左上:藍
ball2_pos = vector( L/2 , L/2 , 0) #右上:黃
ball3_pos = vector( L/2 ,-L/2 , 0) #右下:紅
ball4_pos = vector(-L/2 ,-L/2 , 0) #左下:綠

ball1 = sphere(pos=ball1_pos, radius=1, make_trail=true, retain=3333, material=materials.earth, color=color.blue)
ball2 = sphere(pos=ball2_pos, radius=1, make_trail=true, retain=3333, material=materials.earth, color=color.yellow)
ball3 = sphere(pos=ball3_pos, radius=1, make_trail=true, retain=3333, material=materials.earth, color=color.red)
ball4 = sphere(pos=ball4_pos, radius=1, make_trail=true, retain=3333, material=materials.earth, color=color.green)

ball1.v = vector( v, v, 0)
ball2.v = vector( v,-v, 0)
ball3.v = vector(-v,-v, 0)
ball4.v = vector(-v, v, 0)

def Calc_Spd_2d(NO): #para: ballNo.
    ball_v = [0, ball1.v, ball2.v, ball3.v, ball4.v]
    return (ball_v[NO].x**2 + ball_v[NO].y**2)**0.5

def Calc_Fg_Vector(NO1, NO2): #para: ballNO.
    ball_pos = [0, ball1.pos, ball2.pos, ball3.pos, ball4.pos] #open an array that stores balls' x
    dist = ((ball_pos[NO1].x-ball_pos[NO2].x)**2+(ball_pos[NO1].y-ball_pos[NO2].y)**2+(ball_pos[NO1].z-ball_pos[NO2].z)**2)**0.5
    radiavector = (ball_pos[NO2]-ball_pos[NO1])/dist
    Fg_vector = Fg(dist)*radiavector #行星所受萬有引力
    return Fg_vector

t = 0 ; dt = 0.001

while True:
    rate(2017)
    # 將純量改為向量
    Fg_vector12 = Calc_Fg_Vector(1,2)
    ball1.v += -Fg_vector12/m*dt #ball1受力 力生加速度, 產生速度變化 
    ball2.v += Fg_vector12/m*dt #ball2受力 力生加速度, 產生速度變化

    Fg_vector13 = Calc_Fg_Vector(1,3)
    ball1.v += -Fg_vector13/m*dt #ball1受力 力生加速度, 產生速度變化 
    ball3.v += Fg_vector13/m*dt #ball3受力 力生加速度, 產生速度變化

    Fg_vector14 = Calc_Fg_Vector(1,4)
    ball1.v += -Fg_vector14/m*dt #ball1受力 力生加速度, 產生速度變化 
    ball4.v += Fg_vector14/m*dt #ball4受力 力生加速度, 產生速度變化  
    
    Fg_vector23 = Calc_Fg_Vector(2,3)
    ball2.v += -Fg_vector23/m*dt #ball2受力 力生加速度, 產生速度變化 
    ball3.v += Fg_vector23/m*dt #ball3受力 力生加速度, 產生速度變化

    Fg_vector24 = Calc_Fg_Vector(2,4)
    ball2.v += -Fg_vector24/m*dt #ball2受力 力生加速度, 產生速度變化 
    ball4.v += Fg_vector24/m*dt #ball4受力 力生加速度, 產生速度變化

    Fg_vector34 = Calc_Fg_Vector(3,4)
    ball3.v += -Fg_vector34/m*dt #ball3受力 力生加速度, 產生速度變化 
    ball4.v += Fg_vector34/m*dt #ball4受力 力生加速度, 產生速度變化

 
    ball1.pos = ball1.pos + ball1.v*dt #ball1開始運動 速度產生位置變化
    ball2.pos = ball2.pos + ball2.v*dt #ball2開始運動 速度產生位置變化
    ball3.pos = ball3.pos + ball3.v*dt #ball3開始運動 速度產生位置變化
    ball4.pos = ball4.pos + ball4.v*dt #ball4開始運動 速度產生位置變化

    if t % 1 >= 0.999: 
        print "t=", t, ": v="
        print Calc_Spd_2d(1), " / ", Calc_Spd_2d(2), " / ", Calc_Spd_2d(3), " / ", Calc_Spd_2d(4)

    t = t+dt
