#J Murphy
#29/03/2021
#this program asks if the player wants to input power ball numbers then draws a power ball number and gives the player a score
import random
import math
pnumber=[0,0,0]
pPower=0
dnumber=[0,0,0]
dPower=0
r=int(0)
correctNum=0
correctPos=0
score=0
tscore=10
t=0
av=0
aga='y'
price=10
#for y in range(1000):
while aga.lower()=='y':
    tscore=tscore-int(price)
    for x in range(0,10):
        for i in range(0,len(dnumber)):
            r=random.randint(1,9)
            #print(r)
            #print(r in dnumber)
            while r in dnumber:
                r=random.randint(1,9)
                #print(r)
                #print(r in dnumber)
            dnumber[i]=r
            #print(r)
    dPower=random.randint(1,9)
    #print(dnumber,dPower)
    rDraw=input("would you like to Quick Pick? (Y/N):")
    #rDraw="y"
    if rDraw=='y' or rDraw=="Y":
        for x in range(0,10):
            for i in range(0,len(pnumber)):
                r=random.randint(1,9)
                #print(r)
                #print(r in dnumber)
                while r in pnumber:
                    r=random.randint(1,9)
                    #print(r)
                    #print(r in dnumber)
                pnumber[i]=r
            #print(r)
        pPower=random.randint(1,9)
    elif rDraw=='n' or rDraw=="N":
        for i in range(0,len(pnumber)):
                r=int(input("enter #"+str(i+1)+":"))
                #print(r)
                #print(r in dnumber)
                while r in pnumber or r > 9 or r < 1:
                    print("error Bad Number")
                    r=int(input("enter #"+str(i+1)+":"))
                    #print(r)
                    #print(r in dnumber)
                pnumber[i]=r
        while pPower >9 or pPower<1:
            pPower=int(input("enter power number:"))
            if pPower>9 or pPower<1:
                print("bad number")
    print("yout ticket:",pnumber,pPower)
    print("the Drawing:",dnumber,dPower)
    for i in range(0,len(dnumber)):
        if pnumber[i] in dnumber:
            correctNum=correctNum+1
        if pnumber[i]==dnumber[i]:
            correctPos=correctPos+1
    if correctNum>0:
        score=(((1*10**correctNum)*(correctPos+1)))
    if pPower==dPower:
        print("you have", correctNum,"correct numbers and",correctPos,"of thoes numbers are in the correct position and you got the power number")
        score=score*10
    else:
        print("you have", correctNum,"correct numbers and",correctPos,"of thoes numbers are in the correct position and you did not get the power number")
    tscore=tscore+score
    print("you won $"+str(score))
    print("you have $"+str(tscore))
   
    
    pnumber=[0,0,0]
    pPower=0
    dnumber=[0,0,0]
    dPower=0
    r=int(0)
    correctNum=0
    correctPos=0
    score=0
    t=t+1
    av=tscore/t
    #print(av)
    
    if tscore>10:
        price=int((1*10**math.log(tscore,10))/2)
    else:
        price=10
    print("price to go again is $"+str(price))
    aga=input("would you like to go again (Y/any key): ")
print("you'r score is $"+str(tscore))
