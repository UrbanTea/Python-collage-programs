import sys
import turtle
import time
import random
s=0
z=0
y=400 #400 is the average size of the screen
fn=""
uin=''
def open_file(file_name, mode):
    try:
        file=open(file_name, mode)
    except IOError as e:
        print("Unable to open file:",str(file_name)+". Is it still there\nEnding program")
        input("\n\nPress enter to exit")
        sys.exit()
    else:
        return file
def map(v,ln,lx,rn,rx):
    ls=lx-ln
    rs=rx-rn
    vs=float(v-ln)/float(ls)
    return rn+(vs*rs)
window=turtle.Screen()
t=turtle.Turtle()
uin=input("would you like the hex file or rgb file or dynamic file [h]/[r]/[d]:")
if uin=="h" or uin=="H":
    t.speed(10)
    fn="hexfile.txt"
    window.colormode(1)
elif uin=='r' or uin=='R':
    t.speed(10)
    fn="rgbfile.txt"
    window.colormode(255)
elif uin=='d' or uin=='D':
    t.speed(0)
    fn="dynfile.txt"
    window.colormode(255)
    file=open_file(str(fn),"w")
    k=int(input("number of circles:"))
    l=255/k
    r=0
    g=0
    b=0
    for i in range(k):
        #print(r,g,b)
        print("◾"*int(map(i,0,k,0,10))+"◽"*int(map(k-i-1,0,k,0,10)))
        r=r+int(map(i,0,k,0,255))
        if r >= 255:
            r=0
            g=g+int(map(i,0,k,0,255))
        if g >= 255:
            g=0
            b=b+int(map(i,0,k,0,255))
        if b >= 255:
            b=0
        h=str(r)+","+str(g)+","+str(b)
        file.write(str(h)+"\n")  
        #h=str(hex(int(i*g)))
    file.close()
else:
    print("error bad input")
file=open_file(str(fn),"r")
print(file)
s=len(file.readlines())
print(s,"lines")
z=y/s
file.close()
file=open_file(str(fn),"r")
t.speed(10)

      
window.bgcolor(0,0,0)
colour=file.readline()

st=s
#t.sety((s*10)-100)
##while colour:
##    colour=colour.strip()
##    print(colour)
##    print(tuple(colour.split(","))[0])
##    colour=file.readline()
while colour:
    colour=colour.strip()
    print(colour,"◾"*int(map(st-s,0,st,0,10))+"◽"*int(map(s-1,0,st,0,10)))
    if uin=="h" or uin=="H":
        t.color(colour)
    else:
        t.color(int(tuple(colour.split(","))[0]),int(tuple(colour.split(","))[1]),int(tuple(colour.split(","))[2]))
    t.penup()
    t.setx(s*z)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.circle(s*z)
    t.right(90)
    #t.right(180)
    t.end_fill()
    s=s-1
    colour=file.readline()
    
    time.sleep(1)
file.close()
