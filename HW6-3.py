# -*- coding: utf-8 -*-
from visual import *

m1 = 1
m2 = 800
g=9.8                 #重力加速度 9.8 m/s^2
size = 2              #球半徑2 m
height_1 = 100.0       #球1初始高度
height_2 = height_1-2*size      #球2初始高度

scene = display(width=400, height=800,x=0, y=0, center = (0,height_1,0), background=(0.3,0.3,0.6)) #設定畫面
floor = box(length=40, height=0.01, width=10, color=color.blue)                         #畫地板
ball_1 = sphere(radius = size, color=color.red ) #畫球
ball_2 = sphere(radius = size, color=color.green ) #畫球


ball_1.pos = vector( 0, size+height_1, 0)        #球初始位置       
ball_1.v = vector( 0, 0, 0)                    #球初速 
ball_2.pos = vector( 0, size+height_2, 0)        #球初始位置       
ball_2.v = vector( 0, 0, 0)                    #球初速 


dt = 0.001                              #時間間隔 0.001 秒
ball1_maxH = 0  #ball1最高

while True:             
    rate(1111)                          #每一秒跑 1000 次
    ball_1.pos += ball_1.v*dt
    ball_1.v.y += - g*dt
    
    if ball_1.y <= size and ball_1.v.y < 0:     
        ball_1.v.y = - 1* ball_1.v.y

    ball_2.pos += ball_2.v*dt
    ball_2.v.y += - g*dt
    
    if ball_2.y <= size and ball_2.v.y < 0:     
        ball_2.v.y = - 1* ball_2.v.y
 


    if abs(ball_1.y-ball_2.y) <= 2*size :
        v1y = (m1-m2)*ball_1.v.y/(m1+m2) + 2*m2*ball_2.v.y/(m1+m2)
        v2y = 2*m1*ball_1.v.y/(m1+m2) + (m2-m1)*ball_2.v.y/(m1+m2)

        ball_1.v.y = v1y
        ball_2.v.y = v2y


    if ball_1.pos.y > ball1_maxH:
    	ball1_maxH = ball_1.pos.y
    	print "Current Max Height:", ball1_maxH
    		


