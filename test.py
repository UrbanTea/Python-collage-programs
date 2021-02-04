import turtle
import math
x=input("input")
#y=input("size")
y=0
z=0
s=0
t=0
xp=0
yp=0
for i in x:
    z=z+1
    if i==" ":
        s=s+1
y=400/z
print(y)
##for i in range(4):
##    turtle.forward(400)
##    turtle.backward(400)
##    turtle.right(90)

turtle.penup()
##turtle.setx((-(z*int(y)))/2)
##turtle.sety((-(z*int(y)))/4)


for i in x:
    
    if i=="a" or i=="A":
        xp=xp+(int(y))
        yp=yp-(int(y))
        t=t+int(y)*2
    if i=="b" or i=="B":
        xp=xp-(int(y))
        yp=yp-(int(y))
    if i=="c" or i=="C":
        xp=xp+(int(y)/3.141592)
        yp=yp+(int(y))
    if i=="d" or i=="D":
        xp=xp-(int(y)*.707)
        yp=yp-(int(y)*.707)
    if i=="e" or i=="e":
        xp=xp+(int(y)*.707)
        yp=yp-(int(y)*.707)
        t=t+int(y)*2
    if i=="f" or i=="F":
        yp=yp+(int(y))
    if i=="g" or i=="G":
        xp=xp-(int(y)/3.141592)
        yp=yp+(int(y))
        t=t+int(y)
    if i=="h" or i=="H":
        xp=xp-(int(y))
        yp=yp+(int(y))
    if i=="i" or i=="I":
        xp=xp-(int(y)/3.141592)
        yp=yp-(int(y))
        t=t+int(y)
    if i=="j" or i=="J":
        xp=xp+(int(y)/2)
        yp=yp-(int(y)/2)
        t=t+int(y)
    if i=="k" or i=="K":
        xp=xp-(int(y)/2)
        yp=yp+(int(y)/2)
    if i=="l" or i=="L":
        xp=xp-(int(y)/2)
        yp=yp-(int(y)/2)
    if i=="m" or i=="M":
        xp=xp-(int(y))
        yp=yp-(int(y))
    if i=="n" or i=="N":
        xp=xp-(int(y))
        yp=yp-(int(y)/3.141592)
    if i=="o" or i=="O":
        xp=xp+(int(y))
        yp=yp-(int(y))
        t=t+int(y)*2
    if i=="p" or i=="P":
        xp=xp+(int(y))
        yp=yp+(int(y))
        t=t+int(y)*2
    if i=="q" or i=="Q":
        turtle.left(180)
        turtle.circle(int(y)*2, 90)
        turtle.left(90)
        t=t+int(y)*2
    if i=="r" or i=="r":
        turtle.right(90)
        turtle.circle(int(y), -90)
        turtle.left(180)
    if i=="s" or i=="S":
        turtle.left(45)
        turtle.forward(int(y))
        turtle.right(45)
    if i=="t" or i=="T":
        turtle.forward(int(y)*2)
    if i=="u" or i=="U":
        turtle.left(270)
        turtle.circle(-int(y), 180)
        turtle.right(90)
        t=t+int(y)
    if i=="v" or i=="V":
        turtle.right(45)
        turtle.forward(int(y)*2)
        turtle.left(45)
    if i=="w" or i=="W":
        turtle.left(270)
        turtle.circle(int(y)*2, 90)
    if i=="x" or i=="X":
        turtle.circle(-int(y)/2, 180)
        turtle.right(180)
        t=t+int(y)/2
    if i=="y" or i=="Y":
        turtle.right(225)
        turtle.forward(int(y)*2)
        turtle.left(225)
        t=t+int(y)*2
    if i=="z" or i=="Z":
        turtle.left(90)
        turtle.circle(int(y), -90)
        t=t+int(y)
    if i==" ":
        xp=xp-(t+(int(y)*1.5)/((s+1)))
        yp=yp/((z+1))
        t=0
t=0
turtle.setx(xp)
turtle.sety(yp)
print(xp,yp,z)
turtle.pendown()       
for i in x:
    
    if i=="a" or i=="A":
        turtle.circle(int(y)*2, -90)
        turtle.left(90)
        t=t+int(y)*2
    if i=="b" or i=="B":
        turtle.circle(int(y)*2, 90)
        turtle.right(90)
    if i=="c" or i=="C":
        turtle.circle(-int(y), -180)
        turtle.right(180)
    if i=="d" or i=="D":
        turtle.left(45)
        turtle.forward(int(y)*2)
        turtle.right(45)
    if i=="e" or i=="e":
        turtle.left(135)
        turtle.forward(int(y)*2)
        turtle.right(135)
        t=t+int(y)*2
    if i=="f" or i=="F":
        turtle.right(90)
        turtle.forward(int(y)*2)
        turtle.left(90)
    if i=="g" or i=="G":
        turtle.circle(-int(y), 180)
        turtle.right(180)
        t=t+int(y)
    if i=="h" or i=="H":
        turtle.circle(-int(y)*2, 90)
        turtle.left(90)
    if i=="i" or i=="I":
        turtle.circle(int(y), 180)
        turtle.right(180)
        t=t+int(y)
    if i=="j" or i=="J":
        turtle.circle(int(y), -90)
        turtle.left(90)
        t=t+int(y)
    if i=="k" or i=="K":
        turtle.circle(-int(y), 90)
        turtle.left(90)
    if i=="l" or i=="L":
        turtle.circle(int(y), 90)
        turtle.right(90)
    if i=="m" or i=="M":
        turtle.right(90)
        turtle.circle(int(y)*2, -90)
        turtle.left(180)
    if i=="n" or i=="N":
        turtle.left(90)
        turtle.circle(-int(y), 180)
        turtle.right(270)
    if i=="o" or i=="O":
        turtle.left(90)
        turtle.circle(int(y)*2, 90)
        turtle.right(180)
        t=t+int(y)*2
    if i=="p" or i=="P":
        turtle.left(90)
        turtle.circle(int(y)*2, -90)
        t=t+int(y)*2
    if i=="q" or i=="Q":
        turtle.left(180)
        turtle.circle(int(y)*2, 90)
        turtle.left(90)
        t=t+int(y)*2
    if i=="r" or i=="r":
        turtle.right(90)
        turtle.circle(int(y), -90)
        turtle.left(180)
    if i=="s" or i=="S":
        turtle.left(45)
        turtle.forward(int(y))
        turtle.right(45)
    if i=="t" or i=="T":
        turtle.forward(int(y)*2)
    if i=="u" or i=="U":
        turtle.left(270)
        turtle.circle(-int(y), 180)
        turtle.right(90)
        t=t+int(y)
    if i=="v" or i=="V":
        turtle.right(45)
        turtle.forward(int(y)*2)
        turtle.left(45)
    if i=="w" or i=="W":
        turtle.left(270)
        turtle.circle(int(y)*2, 90)
    if i=="x" or i=="X":
        turtle.circle(-int(y)/2, 180)
        turtle.right(180)
        t=t+int(y)/2
    if i=="y" or i=="Y":
        turtle.right(225)
        turtle.forward(int(y)*2)
        turtle.left(225)
        t=t+int(y)*2
    if i=="z" or i=="Z":
        turtle.left(90)
        turtle.circle(int(y), -90)
        t=t+int(y)
    if i==" ":
        turtle.penup()
        turtle.forward(t+(int(y)*1.5))
        turtle.sety(yp)
        turtle.pendown()
        t=0
    print(i,t)
turtle.penup()
turtle.sety(0)
turtle.forward(t)
turtle.hideturtle()
print(z)

