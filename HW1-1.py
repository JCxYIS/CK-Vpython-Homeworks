# -*- coding: cp950 -*-
from visual import*
from visual.graph import*

size = 0.48763

scene = display(width=400, height=400, center=(7.5,0,0), background=(0,0,0)) 

x = arrow(pos=vector(0,0,0), axis=vector(10,0,0), shaftwidth=0.2,
          color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,10,0), shaftwidth=0.2,
          color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,10), shaftwidth=0.2,
          color=color.blue)

ball = sphere(radius=size, color= color.orange,
              pos=vector(0,0,0), v=vector(0.0,0.0,0), a = vector(5.0,0,0))

text(text='Yee', align='center', depth=-0.3, color=color.green, pos = vector(0,-1.4,0)) #Yee.

dt = 0.001
t = 0.0

changed1 = False #To modify 'a' on 2 sec
maxX = 0 #max x value.

gd = gdisplay(x=400, y=0, width=400, height=400, xtitle='t',
              ytitle='BLUE:x / RED:v / YELLOW:a', foreground=color.black, background=color.white,xmax=6, xmin=0, ymax=20, ymin=-20)

f1 = gcurve(color=color.blue) #x
f2 = gcurve(color=color.red) #v
f3 = gcurve(color=color.yellow) #a

while t < 6:
    rate(1 / dt)
    t = t+dt

    if t >= 2.0 and changed1 == False:  #modify the 'a' at 2s
        ball.a = vector(-5,0,0)
        changed1 = True

    ball.v = ball.v + ball.a * dt
    
    ball.pos = ball.pos + ball.v*dt

    if ball.pos.x > maxX: #determine if x > maxX 
      maxX = ball.pos.x

    f1.plot(pos=(t,ball.pos.x))
    f2.plot(pos=(t,ball.v.x))
    f3.plot(pos=(t,ball.a.x))


    #print t, "秒, 離出發點" , ball.pos.x  #Lag, but will display more information


print "End! The maximum x =", maxX

