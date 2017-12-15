from visual import *

g = 9.8
A = 0.48763                          #振幅 change dis
N = 50                           #介質個數
omega = 2*pi/1.0       #振動角頻率
size = 0.1                      #介質的大小
m = 0.1                         #介質的質量
k = 500.0                      #彈力常數
d = 0.4                          #介質之間的初始間隔

theta = 0.0 #L2, 西塔腳of球球1
     
scene = display(title='Spring Wave', width=300, height=1200, range = 10, center = (0, -(N-1)*d/2, 0)) 
ball = []
ball.append( sphere(radius=size, color=color.red, pos=vector(A, 0, 0), v=vector(0,0,0) )  )
for i in range(N-1):
    ball.append( sphere(radius=size, color=color.yellow, pos=vector(A, -i*d, 0), v=vector(0,0,0) ) )

#ball = [sphere(radius=size, color=color.yellow, pos=vector(0, -i*d, 0), v=vector(0,0,0) ) for i in range(N)]
spring = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(A, -i*d, 0), axis=vector(A,d,0)) for i in range(N-1)]

def SpringForce(r):#春日之力!!!(?
    return - k*(abs(r)-d)*r/abs(r)

#X = ball[-1].pos
      

t, dt = 0, 0.001
while True:
    rate(1000)
    t += dt    

    theta = theta + omega*dt
    ball[0].pos = vector(A*cos(theta), 0, A*sin(theta))

    #在球與球之間放入彈簧
    #from index 0 to 49, the elements are 0,1, 2, 3, 4,... , 48, totally 49 springs
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    #計算每一個球受相鄰兩條彈簧的彈力
    #from index 1 to 50, the elements are 1, 2, 3, 4,... , 49
    for i in range(1, N):      
        if i == N-1: ball[-1].v += SpringForce(spring[-1].axis)/m*dt
        else: ball[i].v += (-SpringForce(spring[i].axis) + SpringForce(spring[i-1].axis))/m*dt  #非最後且非第一個的球

        ball[i].v.y -= g*dt #重力aff
        ball[i].pos +=  ball[i].v*dt

    #ball[-1].pos = X
    # print X
