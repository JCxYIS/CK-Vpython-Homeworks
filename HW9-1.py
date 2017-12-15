# -*- coding: utf-8 -*-
import colorsys # https://docs.python.org/3/library/colorsys.html#module-colorsys
from visual import *
G=2000
M=1.0
m=1.0
dt = 0.001
t = 0
R = 10
Re = 1
scene = display(width=900, height=900, background=(0.5,0.5,0),range = 1.2*R,title = "AhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhWhyyyyyyyyyyyyyy")
scene.center = (0,0,0)
ball = sphere(pos=vector(0,0.5,0), radius = 0.5, color=color.green)
ball.v = vector(0,0,0)
dist = 0
#1
balllist = []
for N in range(0,360,1):
  balllist.append(sphere(pos=vector(R*cos(N*pi/180),0,R*sin(N*pi/180)), radius = 0.1, color=color.red))

arrowlist = []
for N1 in range(-12,13,1): #X軸
  for N2 in range(-12,13,1):#Y軸
    for N3 in range(0,1,1): #z軸
        arrowlist.append(arrow(pos=vector(N1*Re,N2*Re,N3*Re),axis=vector(0,0,0),shaftwidth=0.1 , color=color.green))

for N in arrowlist:
  Fglist=[]
  for P in range(0,360,1):
      dist = ((N.pos.x-balllist[P].x)**2+(N.pos.y-balllist[P].y)**2+(N.pos.z-balllist[P].z)**2)**0.5
      radiavector = (N.pos-balllist[P].pos)/dist
      Fglist.append(-G*M*m*radiavector/(dist**2))
  #Fg = vector(0, 0, 0)          #每次計算要先歸0 (阿我們又沒Fg
  for K in range(0,360,1):
      N.axis += Fglist[K]*10**(-3.5)
      #print Fglist[K]*10**(-17)
  #print N.axis

  if N.axis.mag>=3: #delete the super long ones
      N.axis = vector(0,0,0)




Yee = text(text='Yee', align='center', depth=1, color=color.green, pos = vector(0,0,0)) #Yee.


'''
  N_dist = ((N.x-earth.x)**2+(N.y-earth.x)**2+(N.z-earth.x)**2)**0.5
  N_radiavector = (N.pos-earth.pos)/N_dist
  if N_dist > 1.2*Re and N_dist < 5*Re:
    N.axis = ag(N_dist) * N_radiavector * 10
  else:
    N.axis = vector(0,0,0)
    '''
prismatic = 0
while True:
    rate(888)
    prismatic += 1
    if prismatic >= 360:
        prismatic = 0
    #print prismatic
    Yee.color = colorsys.hls_to_rgb(prismatic/360.0 , 0.5, 1.0)
