# -*- coding: utf-8 -*-
from visual import *
from visual.graph import*
import colorsys # https://docs.python.org/3/library/colorsys.html#module-colorsyss

N = 50   #How many Balls do you have? (No metaphor included XD)
size = 0.016
SpringThickness = size / 5.0 #as the name says
m = 0.1/N #mass of the (imaginary) ball
k = N*0.5 #Bouncy Rate
AirK = 5.0 #AirResis Rate
d = SpringThickness   #Each distance of Springs
g = vector(0, -9.8, 0) #gg, appeared so many times =) vec3 this time lol!
T0 = 5.0    #彈簧放手之刻 the moment we release the spring
T0_DrawOffset = 1
t, dt = 0, 0.005
pre_ball_cm = [0,0,0] #empty array, will be used later

scene = display(width=400, height =500, center = vector(0, -3*d*N, -2))
Gscene = gdisplay(x=400, y=0, width=400, height=400, xtitle='t', ytitle='v',
foreground=color.black, background=color.white,
xmax=T0+T0_DrawOffset, xmin=T0-T0_DrawOffset, ymax=0, ymin=-10)#設定函數圖的畫面
BottomLine = gcurve(color=color.blue) #設定函數圖中線條的特性,這裡只設定顏色
CenterLine = gcurve(color=color.green) #設定函數圖中線條的特性,這裡只設定顏色
text(text='Yee', align='center', depth=1, color=color.green, pos = vector(0,0,0)) #Yee.


balls = [sphere(radius=0, color=color.yellow) for i in range(N)]
springs = [helix(radius = size/2.0, thickness = SpringThickness, coils = 1, color = colorsys.hls_to_rgb(i / (N * 1.0), 0.5, 1.0) ) for i in range(N-1)]
ball_pos, ball_v = zeros((N, 3)), zeros((N,3))  #N = balls , 3 = vectors(x,y,z)

for i in range(N):
    ball_pos[i][1] = -d*i

print "Init...\nBalls Pos:",ball_pos

while True:
    rate(10000)
    t += dt

    #<!--AHHHHHHHH!!!!!!!!!!!-->
    spring_axis = ball_pos[1:] - ball_pos[:-1]
    b = sum ( spring_axis**2, axis = 1)**0.5
    spring_axis_unit = spring_axis / b[:, newaxis]
    fs = - k * (spring_axis - d*spring_axis_unit)
    fs[b<=d] = 0
    #<!--End Of AHHHHHHHH!!!!!!!!!!!-->


    ball_v[1:-1] += ( fs[:-1] - fs[1:] )/m*dt + g*dt
    ball_v[-1] += ( fs[-1]  )/m*dt + g*dt


    if t > T0:      #設定釋放時機點，t < T0前球1不動，之後球1也受力落下
        ball_v[0] += (- fs[0] )/m*dt + g*dt    #請寫入球1釋放後的受力，使球1開始運動

        for j in range(N-1): #由第1根彈簧算到最個最後1根，個數比球少1個
            if (ball_pos[j][1] - ball_pos[j+1][1]) <= d:  #球和球間距小於彈簧原長
                ball_v[j] = ball_v[j+1] = (ball_v[j] + ball_v[j+1])/2  #碰撞後速度
                ball_pos[j+1][1] = ball_pos[j][1] - d    #碰撞後球的間距

    else: #hasn't released
        ball_v[1:-1] -= 5.0*ball_v[1:-1]*dt  #AirResis
        ball_v[-1] -= 5.0*ball_v[-1]*dt #last ball's AirResis


    ball_pos += ball_v * dt

    for i in range(N):
        balls[i].pos = ball_pos[i]

    for i in range(N-1):
        springs[i].pos = balls[i].pos
        springs[i].axis = balls[i+1].pos - balls[i].pos

    ball_cm = sum(ball_pos, axis = 0) / N  #這是個1維3個元素的array, 植心pos
    scene.center.y = ball_cm[1]
    BottomLine.plot(pos=(t, ball_v[-1][1]) ) #每一個迴圈畫一個點描出線條
    CenterLine.plot(pos=(t, (ball_cm[1]-pre_ball_cm[1])/dt) )
    print ball_cm
    pre_ball_cm = ball_cm
    #print "距離釋放彈簧還剩", T0-t, "秒!!"
