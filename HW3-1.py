
from visual import *
g = 9.8                 
size = 0.05                         
L = 0.5                 
k = 10                  
m = 0.1                 
Fg = m*vector(0,-g,0)  

def SpringForce(r,L):
    return -k*(abs(r)-L)*r/abs(r)

scene = display(width=800, height=800, center=(0, -L*0.9, 0))           
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.yellow)    
ball = sphere(radius = size,  color=color.red)                          
spring = helix(radius=0.02, thickness =0.01)                         
	
ball.pos = vector(0, -L, 0)         
ball.v = vector(0, 0, 0)            

text(text='Yee', align='center', depth=-0.3, color=color.green, pos = vector(0,0,0)) #Yee.


dt = 0.001

#print K/E/U 
KKbox = box(pos=(-0.5,-1.2,0), length=0.2, height=0, width=1, color=color.yellow)
EEbox = box(pos=( 0,-1,0), length=0.2, height=0, width=1, color=color.red)
UUbox = box(pos=(0.5,-1,0), length=0.2, height=0, width=1, color=color.green)

KKtxt = text(text='K', height=0.2, color=color.yellow, pos = vector(-0.5,-1.5,0))
KKtxt = text(text='E', height=0.2, color=color.red, pos = vector(0,-1.5,0)) 
UUtxt = text(text='U', height=0.2, color=color.green, pos = vector(0.5,-1.5,0)) 

while True:
    rate(1000)

    spring.axis = ball.pos - spring.pos 	
    ball.a = (Fg + SpringForce(spring.axis,L))/m
						
    ball.v += ball.a*dt
    ball.pos += ball.v*dt

    Ug = m*g*ball.pos.y
    Us = 0.5*k*(abs(spring.axis)-L)**2
    K = 0.5*m*abs(ball.v)**2
    E = -(Ug + Us + K)

    KKbox.height = K            #modify kkbox's height to k
    EEbox.height = E            #same above
    UUbox.height = 1+ Ug + Us   #because Ug+Us might be negative, thus we plus 1 to avoid this

    print "K=", K ,"/E=", E, "/U=", Ug+Us 
