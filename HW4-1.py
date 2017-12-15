from visual.graph import * 
from visual import *  

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re
V0 = (G*M/H)**0.5 

def Fg(x):                                 
    return -G*M*m/(x**2)

scene = display(width=1200, height=1000, center=(0,5,0),  
                background=color.black)

earth = sphere(pos=vector(0,0,0), radius=Re, material=materials.earth) 
mater = sphere(pos=(H,0,0), radius=0.1*Re,material = materials.wood, make_trail=true, retain=123456)
materv = vector(0,0.7*V0,0)

#gd = gdisplay(x=800,y=0,width=600,height=600, title='Fg', xtitle='R', ytitle='Fg(red)',  foreground=color.black,background=color.white,  xmax=20, xmin=-2, ymax=1.2, ymin=0) 
#f1 = gcurve(color=color.red)  
Fe = G*M*m/Re**2
pre_mater_pos = vector(0,0,0) 

'''
oval = curve( color = color.black )
for N in range(0, 360, 1):
    oval.append( pos =(2.119*10**7*cos(N*pi/180)+1*(2.119**2-1.8228**2)**0.5*10**7,1.8228*10**7*sin(N*pi/180),0) )
'''

#sum_area = 0.0

v_arrow = arrow(pos=mater.pos,axis=(0,0,0),shaftwidth=0.4*mater.radius ,color = color.red)
a_arrow = arrow(pos=mater.pos,axis=(0,0,0),shaftwidth=0.4*mater.radius ,color = color.white)
aT_vector = arrow(pos=mater.pos, axis=(0,0,0), shaftwidth = 0.4*mater.radius ,color=color.yellow) #At's arrow
aN_vector = arrow(pos=mater.pos, axis=(0,0,0), shaftwidth = 0.4*mater.radius ,color=color.blue) #An's arrow

yee = text(text='Yee', align='center', height = Re, depth = Re, color=color.green, pos = vector(H/2,0,0)) #Yee.

t = 0 ; dt = 1
while True:  
    rate(1000)
    '''
    pre_pre_mater_pos = pre_mater_pos    
    pre_mater_pos = vector(mater.pos.x , mater.pos.y, mater.pos.z) 
    '''
    dist = ((mater.x-earth.x)**2+(mater.y-earth.x)**2+(mater.z-earth.x)**2)**0.5 
    radiavector = (mater.pos-earth.pos)/dist 
    Fg_vector = Fg(dist)*radiavector 
    
    materv += Fg_vector/m*dt   
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt

    v_arrow.pos = mater.pos
    a_arrow.pos = mater.pos
    v_arrow.axis = materv*2*10**3 
    a_arrow.axis = Fg_vector/m*2*2*10**6 

    aT = dot(a_arrow.axis,v_arrow.axis)*(norm(v_arrow.axis)/mag(v_arrow.axis))
    aN = (mag(cross(a_arrow.axis,v_arrow.axis)) / mag(v_arrow.axis)) * cross( norm(v_arrow.axis), cross(norm(a_arrow.axis), norm(v_arrow.axis) ) )
    
    aT_vector.axis = aT  #point at aT
    aN_vector.axis = aN
    aT_vector.pos = mater.pos #make it follow the ball
    aN_vector.pos = mater.pos

    '''
    a = mag(mater.pos-earth.pos)  
    b = mag(earth.pos-pre_mater_pos)
    c = mag(pre_mater_pos-mater.pos)
    s = (a+b+c)/2                
    '''
    '''
    area = (s*(s-a)*(s-b)*(s-c))**0.5 
    sum_area += area            
    '''

    '''
    if t >= 2785 :
        print t , sum_area
        t = 0
        sum_area = 0
        cylinder(pos=earth.pos, axis=mater.pos-earth.pos, radius=0.01*Re, color=color.black) 
    '''

    t = t+dt

    '''
    if pre_mater_pos.x > pre_pre_mater_pos.x and pre_mater_pos.x > mater.pos.x :        
            print mater.pos    
    if pre_mater_pos.x < pre_pre_mater_pos.x and pre_mater_pos.x < mater.pos.x :        
            print mater.pos    
    if pre_mater_pos.y > pre_pre_mater_pos.y and pre_mater_pos.y > mater.pos.y :        
            print mater.pos    
    if pre_mater_pos.y < pre_pre_mater_pos.y and pre_mater_pos.y < mater.pos.y :        
            print mater.pos 
    '''
  
    #f1.plot(pos=(mater.x/Re,mag(Fg_vector)/Fe))




