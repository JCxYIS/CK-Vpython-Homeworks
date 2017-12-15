# -*- coding: utf-8 -*-
import colorsys # https://docs.python.org/3/library/colorsys.html#module-colorsys
from visual import *
import random

k = 9*10**9
size = 0.1  # charge size
QofLittleBall = 10 **(-7) #小球的Q
MofLittleBall = 10 **(-3) #小球的M

b_N = 20

Q1_charge = 1*10**(-5) #Q1電量
Q1_position = vector(0, 0, 0) #Q1位置

Q2_charge = -1*10**(-5) #Q2電量
Q2_position = vector(2, 0, 0) #Q2位置


scene = display(title='Dipole...With Mouse and Keyboard Control!', height=5000, width=5000, range=3.5,
                auto_scale=False, background=(0,0,0))

Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2 = sphere(pos = Q2_position , radius = size , color = color.red)

field_ball_1=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q1_position,
                             radius=0.01, color=(1,1,0), make_trail=True, v=vector(0,0,0)))

field_ball_2=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q2_position,
                             radius=0.01, color=(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

def Force_E(r, q):#force of field
    r0 = r - Q1_position
    r1 = r - Q2_position
    return k*q*Q1_charge*r0.norm()/(r0.mag*r0.mag)+k*q*Q2_charge*r1.norm()/(r1.mag*r1.mag)

Yee = text(text='Yee', align='center', depth=2, color=color.red, pos = vector(-1,0,0), height = 0.3, font = "c:/windows/fonts/xolonium-bold.ttf") #Yee.
prismatic = 0

q_charge = 1 * 10 **(-7)
q_position = vector (1 , 1 , 0)
q_m = 10**(-3)
q_v = vector (0 , 0 , 0)

q = sphere(pos = q_position , radius = 0.2*size , color = color.green , make_trail=True)
q.v = q_v

Lab = label(text='Left click to place\n balls.', pos=(-2.5,-1.5,0), opacity=0.2)

LittleBall = [];
def makeSphere(evt):
    loc = evt.pos
    RdmColor = colorsys.hls_to_rgb(random.uniform(0, 360)/360.0 , 0.5, 1.0)
    print "Instantiating Ball at ", loc
    LittleBall.append(sphere(pos=loc, radius=size/2.0, color = RdmColor ,make_trail=True,
                       v=vector(0,0,0), a=vector(0,0,0), q=QofLittleBall, m=MofLittleBall))
scene.bind('mousedown', makeSphere, scene)

def keyinput(evt):                # keyboard interrupt callback function
    global QofLittleBall, MofLittleBall
    Qadj = {'q' : 10 **(-7), 'w':-10 **(-7)}
    Madj = {'o':10 **(-3), 'p':-10 **(-3)}

    s = evt.key
    if s in Qadj :
        QofLittleBall += Qadj[s]
        print "Adjusting Q to " , QofLittleBall* 10**(7), "/10**7"
    if s in Madj :
        MofLittleBall += Madj[s]
        print "Adjusting M to " , MofLittleBall* 10**(3), "/10**3"
scene.bind('keydown', keyinput)                    # the binding method

dt = 0.001
while True:
    rate(1000)

    prismatic += 0.248763
    if prismatic >= 360:
        prismatic = 0
    #print prismatic
    Yee.color = colorsys.hls_to_rgb(prismatic/360.0 , 0.5, 1.0)

    for N in field_ball_1:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for JC in field_ball_2:
        JC.v = Force_E(JC.pos, -1.0).norm()
        JC.pos += JC.v*dt

    for YIS in LittleBall:
        YIS.v += Force_E(YIS.pos, YIS.q)/YIS.m * dt
        YIS.pos += YIS.v*dt


    q.v = q.v + Force_E(q.pos, q_charge)/q_m *dt
    q.pos = q.pos+q.v*dt

    Lab.text = "If you instantiate a ball now,\n"
    Lab.text += "Q will be " + str(QofLittleBall* 10**(7))+ " / (10**7) (Press Q/W to modify)\n"
    Lab.text += "M will be " + str(MofLittleBall* 10**(3))+ " / (10**3) (Press O/P to modify)"

'''
    if abs(q.pos-Q1_position)<=size or abs(q.pos-Q2_position)<=size :
        break

while True:
    rate(1000)
'''
