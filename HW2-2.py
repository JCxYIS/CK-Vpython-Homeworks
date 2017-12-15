from visual import *

g = 9.8             #���O�[�t�� 9.8 m/s^2
size = 0.5          #�y�b�| 0.5 m

scene = display(width=600, height=600,x=0, y=0, background=color.black ) #�e��

floor = box(length=24.8763, height=0.01, width=24.8763, color=color.green)  #�e�a�O

ball = sphere(radius = size, color=color.yellow,
              make_trail= True) #���ڭ̨ӵe�f�R���p�y

text(text='Yee', align='center', height= 7, depth=-0.93, color=color.green, pos = vector(0,4,0)) #Yee.

dt = 0.001     #�ɶ����j 0.001 ��


v0 = 14.8763 #�o �g �t ��
angle = 0.0
timer = 0.0
stopped = False

while angle * (180 / pi) <= 180:    #����
    rate(1000)        #�C�@��] 1000 ��
 
    timer += dt

    if ball.pos.y <= size:
        stopped = True
        print "Launch Angle : " , angle * (180/pi), " / Fly Distance :�@" , ball.pos.x, " \ Fly Time :�@" , timer
        
        angle = angle + 3 * (pi / 180)   #�C���j��W�[���� 3 ��
        ball.pos = vector(0.0, 0.5, 0)        #��m���]
        ball.v = vector(v0 * cos(angle), v0 * sin(angle), 0) #�t�׭��]
        timer = 0 #�ɶ�reset
        
        stopped = False

    
    if stopped == False:
        ball.pos = ball.pos + ball.v * dt
        ball.v.y = ball.v.y - g*dt

    
       

    


