# -*- coding: utf-8 -*-
from visual import *
from visual.graph import *

m1 = 5.487                  #球1質量
x1 = -40.0                  #球1X軸初位置
v1= 18.787                    #球1初速度
size1 = 1.487                 #球1大小

m2 = 5.487                   #球2質量
x2 = 0.0                   #球2X軸初位置
y2 = 2.0111
v2 = 0.0                   #球2初速度
size2 = 1.487                 #球2大小

#Force = 5.0               #彈力大小
spring_k = 48763.1               #彈力常數 
spring_L = 8.7            #彈簧長度 

scene = display(width=1200, height=600, background=(0.5,0.5,0), center=(0,0,0),forward=(0,-0.5,-1),range=87)#設定畫面
ball1 = sphere(radius=size1, color = color.red, make_trail=True)  #設定球1
ball1.pos = vector(x1,0,0)             #球1位置
ball1.v = vector (v1,0,0)                        #球1的速度
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue, make_trail=True) #設定球2
ball2.pos = vector(x2,y2,0)             #球2位置
ball2.v = vector (v2,0,0)                        #球2的速度
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.red)

spring = helix(pos=ball2.pos, radius=0.5, thickness =0.1) #畫彈簧
spring.coils = 10
spring.axis = vector(-spring_L,0,0)

t = 0                                            #時間
dt = 0.001   


while True :
    rate(1000)

    collidedTime = 0
    if abs(ball2.pos - ball1.pos) <= spring_L :
        ball1_a = -1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - ( ball2.pos.x - ball1.pos.x )) / m1
        ball2_a = 1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - ( ball2.pos.x - ball1.pos.x )) / m2
        spring.axis = ball1.pos-ball2.pos 
        collidedTime = t
    else :
        ball1_a=vector(0,0,0)
        ball2_a=vector(0,0,0)
        spring.axis = vector(-spring_L,0,0)

    if collidedTime + 3 < t: 
        cos_theta = dot(ball1.v,ball2.v) / (ball1.v.mag*ball2.v.mag)
        theta = acos(cos_theta)*360/(2*pi)
        print theta



    #spring.axis = ball1.pos-ball2.pos 

    ball1.v +=  ball1_a *dt
    ball2.v +=  ball2_a *dt


    ball1.pos = ball1.pos+ball1.v*dt  #控制球1的運動
    ball2.pos = ball2.pos+ball2.v*dt  #控制球2的運動
    

    v1_arrow.pos = ball1.pos #球1速度向量箭頭的起始點在球1上
    v1_arrow.axis = ball1.v  #球1速度向量箭頭的長度與方向等於球1速度

    v2_arrow.pos = ball2.pos #球2速度向量箭頭的起始點在球2上
    v2_arrow.axis = ball2.v  #球1速度向量箭頭的長度與方向等於球2速度

    spring.pos=ball2.pos  #彈簧的起始點位置在球2上



    t=t+dt



