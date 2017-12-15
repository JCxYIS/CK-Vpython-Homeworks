from visual import *

g = 9.8             #���O�[�t�� 9.8 m/s^2
size = 0.5          #�y�b�| 0.5 m
height = 15.0       #�y��l���� 15 m
k = 0.1487630009487594878787878787000000800092000 #�Ū��Y��,���V

scene = display(width=600, height=600,x=0, y=0,
                center = (0,height/2,0), background=(0.5,0.5,0)) #�]�w�e��
floor = box(length=28, height=0.01, width=28, color=color.green)  #�e�a�O
ball = sphere(radius = size, color=color.yellow,
              make_trail= True, trail_type="points", interval=100) #�e�y
Newball = sphere(radius = size, color=color.red,
              make_trail= True, trail_type="points", interval=100) #�e�y�y
Newtonball = sphere(radius = size, color=color.green,
              make_trail= True, trail_type="points", interval=100) #�e�y�y�y

text(text='Yee', align='center', height= 7, depth=-0.93, color=color.green, pos = vector(0,4,0)) #Yee.


ball.pos = vector(0, size, 0)        #�y��l��m       
ball.v = vector( 3, 18.763 , 0)              #�y��t

Newball.pos = vector(0, size, 0)       #�y��l��m       
Newball.v = vector( 3, 18.763 , 0)              #�y��t

Newtonball.pos = vector(0, size, 0)
Newtonball.v = vector( 3, 18.763, 0)

dt = 0.001                              #�ɶ����j 0.001 ��
t = 0.0

while ball.pos.y >= 0 and Newball.pos.y >= 0 and Newtonball.pos.y >= 0: 
    rate(1000)                          #�C�@��] 1000 ��

    t = t + dt    #timer
    
    ball.pos = ball.pos + ball.v * dt
    ball.v.y = ball.v.y - g*dt

    Newball.pos = Newball.pos + Newball.v * dt
    Newball.v.y = Newball.v.y - g*dt
    AirResistance = -k * Newball.v    #��Ū�
    Newball.v += AirResistance * dt   #�[�Ū�

    Newtonball.pos.x = Newtonball.v.x*(1-exp(-k*t))/k   #�M����
    Newtonball.pos.y = -g*t/k + (k*Newtonball.v.y+g)*(1-exp(-k*t))/k**2   #�M����

 

  

    


