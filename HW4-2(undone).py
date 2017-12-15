from visual.graph import * 
from visual import *  
'''
G = 6.67*10**(-11) ; #Gravitational constant
M = 6*10**24 ;  #mass of Earth
m = 1000  #little ball's mass
Re = 6.4*10**6 ; #radius of Earth
H = 5*Re  #litttle ball's distance to Earth
V0 = (G*M/H)**0.5 #little ball's velocity0
Fe = G*M*m/Re**2 #Gravity on earth surface
'''
G = 6.67408 * 10**(-11) ; #Gravitational constant
SunMass = 1.9891 * 10**30
SunRadius = 695500000 
EarthSunDist = 149597870700 
EarthMass = 5.97237 * 10**24
EarthRadius = 6378100
MarsSunDist = 227936640000
MarsMass = 6.4185 * 10**23
MarsRadius = 3396200

def Fg(LittleMass, CurDist):                                 
    return -G * SunMass * LittleMass / (CurDist**2)

scene = display(width=1200, height=1000, center=(0,5,0),  
                background=color.black)

Sun = sphere(pos=vector(0,0,0), radius=SunRadius, color=(253.0/255, 92.0/255, 2.0/255)) 
Earth = sphere(pos=vector(EarthSunDist,0,0), radius=EarthRadius, material=materials.earth, make_trail=true, retain=487630)
Mars = sphere(pos=vector(MarsSunDist,0,0), radius=MarsRadius, color=(208.0/255, 142.0/255, 84.0/255), make_trail=true, retain=487630)

EarthV = vector(0, (G*SunMass/EarthSunDist)**0.5, 0)
MarsV = vector(0, (G*SunMass/MarsSunDist)**0.5, 0)
'''
earth = sphere(pos=vector(0,0,0), radius=Re, material=materials.earth) 
mater = sphere(pos=(H,0,0), radius=0.1*Re, material = materials.wood, make_trail=true, retain=123456)
materv = vector(0,V0,0)
'''
#gd = gdisplay(x=800,y=0,width=600,height=600, title='Fg', xtitle='R', ytitle='Fg(red)',  foreground=color.black,background=color.white,  xmax=20, xmin=-2, ymax=1.2, ymin=0) 
#f1 = gcurve(color=color.red)  

'''
oval = curve( color = color.black )
for N in range(0, 360, 1):
    oval.append( pos =(2.119*10**7*cos(N*pi/180)+1*(2.119**2-1.8228**2)**0.5*10**7,1.8228*10**7*sin(N*pi/180),0) )
'''

#sum_area = 0.0
'''
v_arrow = arrow(pos=mater.pos,axis=(0,0,0),shaftwidth=0.4*mater.radius ,color = color.red)
a_arrow = arrow(pos=mater.pos,axis=(0,0,0),shaftwidth=0.4*mater.radius ,color = color.white)
aT_vector = arrow(pos=mater.pos, axis=(0,0,0), shaftwidth = 0.4*mater.radius ,color=color.yellow) #At's arrow
aN_vector = arrow(pos=mater.pos, axis=(0,0,0), shaftwidth = 0.4*mater.radius ,color=color.blue) #An's arrow
'''
yee = text(text='Yee', align='center', height = 6.4*10**6, depth = 6.4*10**6, color=color.green, pos = vector(EarthSunDist/2,0,0)) #Yee.
pre_mater_pos = vector(0,0,0) 

t = 0 ; dt = 1
while True:  
    rate(1000)
    '''
    pre_pre_mater_pos = pre_mater_pos    
    pre_mater_pos = vector(mater.pos.x , mater.pos.y, mater.pos.z) 
    '''

    CurSEdist = ((Earth.x-Sun.x)**2+(Earth.y-Sun.x)**2+(Earth.z-Sun.x)**2)**0.5 
    radiavector = (Earth.pos-Sun.pos) / CurSEdist 
    Fg_vector = Fg(EarthMass,CurSEdist)*radiavector 

    EarthV += Fg_vector / EarthRadius*dt   
    print EarthV
    Earth.pos = Earth.pos + EarthV*dt  # S = S0 + v *dt

    '''
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




