from visual.graph import*
from visual import *
m = 48763
g = 9.8
size = 0.05
L  = 0.5 
theta = 40.0 * pi / 180 
k = 94870487.630
#/100?

def SpringForce(r):
 return -k * (abs(r) - L) * r / abs(r) 

scene = display(width=600, height=500,center = (0, -L/2, 0), background=(0,0,0))
gd = gdisplay(x=400, y=0, width=400, height=400, xtitle='t', ytitle='E', foreground=color.black, background=color.white,xmax=15, xmin=0, ymax=200000, ymin=-200000)
bC = gcurve(color=color.red) #ball's
gbC= gcurve(color=color.green) #gball's
EC = gcurve(color=color.blue) #system's E's

PhysicsSucks = sphere(radius = size, color=color.yellow)
ball = sphere(radius = size, color=color.red, make_trail=True, retain=5487)
gball = sphere(radius = size, color=color.green, make_trail=True, retain=5487) 
rod1 = cylinder(pos=(0,0,0), radius=0.003) 
rod2 = cylinder(pos=(L,0,0), radius=0.003) 

PhysicsSucks.pos = vector(0, 0, 0) #Ji dian
ball.pos = vector(L, 0, 0) 		   #dan bai
gball.pos = vector(2*L, 0, 0)	   #shoun bai

ball.v = vector(0,0,0) 
gball.v = vector(0,0,0) 

text(text='Yee', align='center', height= 1, depth=-0.93, color=color.green, pos = vector(0,0,0)) #Yee.

dt = 0.001 
t = 0.0

while True:
 rate(1000) 

 t += dt 

 rod2.pos = ball.pos 
 rod1.axis = vector(ball.pos) 
 rod2.axis = gball.pos - ball.pos

 F1 = (vector(0,-m*g,0) + SpringForce(rod1.axis) - SpringForce(rod2.axis) ) 
 F2 = (vector(0,-m*g,0) + SpringForce(rod2.axis) )

 ball.v += F1 / m *dt
 ball.pos += ball.v * dt
 gball.v += F2 / m *dt
 gball.pos += gball.v * dt


 bUg = m*g*ball.pos.y 				#ball's Ug, not bug XD
 bUs = 0.5*k*(abs(rod1.axis)-L)**2  #ball's Us, not bus XD
 bK = 0.5*m*abs(ball.v)**2			#ball's Ek
 bE = bUg + bUs + bK 				#ball's Energy!

 gbUg = m*g*gball.pos.y
 gbUs = 0.5*k*(abs(rod2.axis)-L)**2
 gbK = 0.5*m*abs(gball.v)**2
 gbE = gbUg + gbUs + gbK

 print "ballE=",bE, "gballE=", gbE, "systemE=", bE+gbE
 bC.plot(pos=(t,bE))
 gbC.plot(pos=(t,gbE))
 EC.plot(pos=(t,bE + gbE))

