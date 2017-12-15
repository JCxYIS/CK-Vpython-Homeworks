from visual import *

g = 9.8             #重力加速度 9.8 m/s^2
size = 0.5          #球半徑 0.5 m

scene = display(width=600, height=600,x=0, y=0, background=color.black ) #畫面

floor = box(length=24.8763, height=0.01, width=24.8763, color=color.green)  #畫地板

ball = sphere(radius = size, color=color.yellow,
              make_trail= True) #讓我們來畫口愛的小球

text(text='Yee', align='center', height= 7, depth=-0.93, color=color.green, pos = vector(0,4,0)) #Yee.

dt = 0.001     #時間間隔 0.001 秒


v0 = 14.8763 #發 射 速 度
angle = 0.0
timer = 0.0
stopped = False

while angle * (180 / pi) <= 180:    #模擬
    rate(1000)        #每一秒跑 1000 次
 
    timer += dt

    if ball.pos.y <= size:
        stopped = True
        print "Launch Angle : " , angle * (180/pi), " / Fly Distance :　" , ball.pos.x, " \ Fly Time :　" , timer
        
        angle = angle + 3 * (pi / 180)   #每次迴圈增加仰角 3 度
        ball.pos = vector(0.0, 0.5, 0)        #位置重設
        ball.v = vector(v0 * cos(angle), v0 * sin(angle), 0) #速度重設
        timer = 0 #時間reset
        
        stopped = False

    
    if stopped == False:
        ball.pos = ball.pos + ball.v * dt
        ball.v.y = ball.v.y - g*dt

    
       

    


