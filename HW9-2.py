import colorsys
from visual import *
k = 9*10**9 ;
size = 0.1  ;
b_N = 36
scene = display(title='dipole', height=5000, width=5000, range=8.763,
                auto_scale=False, background=(40.0/255.0,40.0/255.0,40.0/255.0))
#設上球Q1, 右Q2, 下Q3, 左Q4
Q1_charge = -1 * 10**(-5) #Q1電量
Q1_position = vector(0, 2, 0) #Q1位置
Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2_charge = 10**(-5) #Q2電量
Q2_position = vector(2, 0, 0) #Q2位置
Q2 = sphere(pos = Q2_position , radius = size , color = color.red)
Q3_charge = -1 * 10**(-5) #Q3電量
Q3_position = vector(0, -2, 0) #Q3位置
Q3 = sphere(pos = Q3_position , radius = size , color = color.blue)
Q4_charge = 10**(-5) #Q4電量
Q4_position = vector(-2, 0, 0) #Q4位置
Q4 = sphere(pos = Q4_position , radius = size , color = color.red)

q_charge = 1 * 10 **(-7)
q_position = vector (1 , 1 , 0)
q_m = 10**(-3)
q_v = vector (0.0 ,  0.0 , 0.0)
q = sphere(pos = q_position , radius = 0.2*size , color = color.green , make_trail=True)
q.v = q_v

Yee = text(text='Yee', align='center', depth=1, color=color.green, pos = vector(0,0,0), height = 0.48763) #Yee.

field_ball_1=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q1_position,
                             radius=0.01, color=(1,1,0), make_trail=True, v=vector(0,0,0)))

field_ball_2=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q2_position,
                             radius=0.01, color=(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

field_ball_3=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_3.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q3_position,
                             radius=0.01, color=(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

field_ball_4=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_4.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q4_position,
                             radius=0.01, color=(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

def Force_E(r, q):#force of field
    r0 = r - Q1_position
    r1 = r - Q2_position
    r2 = r - Q3_position
    r3 = r - Q4_position
    return ( k*q*Q1_charge*r0.norm()/(r0.mag*r0.mag)
           + k*q*Q1_charge*r2.norm()/(r2.mag*r2.mag)
           + k*q*Q1_charge*r3.norm()/(r3.mag*r3.mag)
           + k*q*Q2_charge*r0.norm()/(r0.mag*r0.mag)
           + k*q*Q2_charge*r1.norm()/(r1.mag*r1.mag)
           + k*q*Q2_charge*r3.norm()/(r3.mag*r3.mag)
           + k*q*Q3_charge*r0.norm()/(r0.mag*r0.mag)
           + k*q*Q3_charge*r1.norm()/(r1.mag*r1.mag)
           + k*q*Q3_charge*r2.norm()/(r2.mag*r2.mag)
           + k*q*Q4_charge*r1.norm()/(r1.mag*r1.mag)
           + k*q*Q4_charge*r2.norm()/(r2.mag*r2.mag)
           + k*q*Q4_charge*r3.norm()/(r3.mag*r3.mag) )

dt = 0.005
prismatic = 0
while True:
    rate(48763)

    for N in field_ball_1:
        N.v = Force_E(N.pos, -1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_2:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_3:
        N.v = Force_E(N.pos, -1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_4:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    q.v = q.v + Force_E(q.pos, q_charge)/q_m *dt
    q.pos = q.pos+q.v*dt
    if abs(q.pos-Q1_position)<=size or abs(q.pos-Q2_position)<=size :
        break



    prismatic += 1
    if prismatic >= 360:
        prismatic = 0
    #print prismatic
    Yee.color = colorsys.hls_to_rgb(prismatic/360.0 , 0.5, 1.0)
