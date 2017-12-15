import colorsys # https://docs.python.org/3/library/colorsys.html#module-colorsys
from visual import *
g = 9.8               
theta = 10*pi/180         #初始擺角設定
k = 100000                     #彈力常數
m = 1.0                            #擺錘的質量
n = 87                              #單擺個數
d = 0.1                             #每個擺錘之間的間隔為d公尺 
size = d/3.5                     #擺錘圓球半徑的大小

L = [] #每一根擺桿的長度
T0 = 3 #擺長最長的擺錘擺N次
N = 20.0 #最長擺錘週期
def CalcFXCKINGPWLength(NO):
    NO += 1
    return g * ( ( (1/(2*pi)) * ( N*T0 / ( N + (NO-1)) ) )**2  )

for lol in range(0,n,1):
    L.append( CalcFXCKINGPWLength(lol) )
    print lol, "//" , CalcFXCKINGPWLength(lol)
#print L

#L = [3.10, 3.26, 3.42, 3.59, 3.76, 3.93, 4.11, 4.29, 4.47, 4.66, 4.85, 5.05]      #每一根擺桿的長度


def SpringForce(r,L):
    return - k*(mag(r)-L) * r / mag(r)

scene = display(width=600, height=800, center = (0, -L[n/2]/2-d, d*n/2+1.5), background=(0,0,0), range=0.9)     
ceiling = box(pos=vector(0,0,(n-1)*d/2), length=0.03, height=0.001, width=(n-1)*d*1.01, color=(0.7,0.7,0.7))    

ball = []
string = []
for i in range(0,n,1):      #0~11
    MyColor = colorsys.hls_to_rgb(i / (n * 1.0), 0.5, 1.0) #彩色珍珠音調!!(誤
    ball.append(sphere(pos=vector(L[i]*sin(theta), -L[i]*cos(theta), d*i),
                       v=vector(0,0,0), radius=size, color=MyColor))
    string.append(cylinder(pos=vector(0,0,d*i), color=MyColor, radius=0.001))

dt = 0.001
t = 0

#print colorsys.hls_to_rgb(135.0 / 255.0, 0.5, 1.0)
text(text='Yee', align='center', depth=1, color=color.green, pos = vector(0,0,0)) #Yee.

while True:
    rate(1/dt)
    t = t+dt

    a = []
    for j in range(0,n,1):
        string[j].axis = ball[j].pos - string[j].pos
        a.append(vector(0,-g,0)+SpringForce(string[j].axis, L[j])/m)
        ball[j].v += a[j]*dt
        ball[j].pos += ball[j].v*dt


        
