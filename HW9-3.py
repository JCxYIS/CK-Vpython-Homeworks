# -*- coding: utf-8 -*-
import colorsys
from visual import *
HelmholtzCoilStyle = "trans" #PARAMETER: "cis"(順) or "trans"(反)
Mu = 4*pi*1e-7 ;
i = 0.5 ;
m = 87e-3/6e23 ;
r = 0.087;
dt = 1e-4 ;
t = 0
scene = display(width=5000, height=5000, background=(0.5,0.5,0), range=0.2487, autoscale=False, title="HelmholtzCoil")

current_vector = []    #線圈電流List
for c in range(0,360,1):
  current_vector.append(arrow(pos=vector(r*cos(c*pi/180),-0.5*r,r*sin(c*pi/180)),
axis=vector(2*pi*r/360*cos(c*pi/180 + pi/2),0,2*pi*r/360*sin(c*2*pi/360 + pi/2)),shaftwidth=0.0005 , color=color.blue))
  if HelmholtzCoilStyle == "cis":
      current_vector.append(arrow(pos=vector(r*cos(c*pi/180),+0.5*r,r*sin(c*pi/180)),
      axis=vector(2*pi*r/360*cos(c*pi/180 + pi/2),0,2*pi*r/360*sin(c*2*pi/360 + pi/2)),shaftwidth=0.0005 , color=color.blue))
  elif HelmholtzCoilStyle == "trans":
      current_vector.append(arrow(pos=vector(r*cos(c*pi/180),+0.5*r,r*sin(c*pi/180)),
      axis=vector(-2*pi*r/360*cos(c*pi/180 + pi/2),0,-2*pi*r/360*sin(c*2*pi/360 + pi/2)),shaftwidth=0.0005 , color=color.green))


def magnatic_1(b,c,d):  #b是空間中任一點位置，c是線圈電流的位置, d是線圈電流的單位長度向量
    R = b-c
    return Mu*i*cross(d,R)/((R.mag**3)*4*pi)


arrowlist = []
for N1 in range(-13,12,1): #X軸
  for N2 in range(0,1,1): #Z軸
    for N3 in range(-11,10,1):#Y軸
      arrowlist.append(arrow(pos=vector(N1*0.01,N3*0.01,N2*0.01),axis=vector(0,0,0),shaftwidth=0.0005 , color=color.red))


for N in arrowlist:
    for M in range(0,360,1):
        N.axis += magnatic_1(N.pos,current_vector[M].pos,current_vector[M].axis)*4876.3 /1.5



Yee = text(text='Yee', align='center', depth=0.002, color=color.green, pos = vector(0,0,0), height = 0.02, font = "c:/windows/fonts/xolonium-bold.ttf") #Yee.
prismatic = 0
while True:
    rate(888)
    prismatic += 1
    if prismatic >= 360:
        prismatic = 0
    print prismatic
    Yee.color = colorsys.hls_to_rgb(prismatic/360.0 , 0.5, 1.0)
