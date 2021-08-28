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
pp=0
tpp=0
ppp=0
gp=0
pgp=0
tgp=0
epe=0
ep=0
tep=0
psp=0
sp=0
tsp=0
pcp=0
cp=0
tcp=0
print("platnum peices = 10 gold peices, gold peices = 2 electrum peices, electrum peices = 5 silver peices, silver peices = 10 copper peices, copper peices = 1 cent")
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
        score=(((1*10**int(correctNum)/10)*((correctPos+1))))
    if pPower==dPower:
        print("you have", correctNum,"correct numbers and",correctPos,"of thoes numbers are in the correct position and you got the power number")
        score=score*10
    else:
        print("you have", correctNum,"correct numbers and",correctPos,"of thoes numbers are in the correct position and you did not get the power number")
    tscore=tscore+score
    pp=math.floor(score/1000)
    score=score-pp*1000
    gp=math.floor(score/100)
    score=score-gp*100
    ep=math.floor(score/50)
    score=score-ep*50
    sp=math.floor(score/10)
    score=score-sp*10

    tpp=math.floor(tscore/1000)
    tscore=tscore-tpp*1000
    tgp=math.floor(tscore/100)
    tscore=tscore-tgp*100
    tep=math.floor(tscore/50)
    tscore=tscore-tep*50
    tsp=math.floor(tscore/10)
    tscore=tscore-tsp*10
    print("you won ",end="")
    if pp>0:
        print("Pp",str(pp),end=" ")
    if gp>0:
        print("Gp"+str(gp),end=" ")
    if ep>0:
        print("Ep"+str(ep),end=" ")
    if sp>0:
        print("Sp"+str(sp),end=" ")
    if cp>0:
        print("Cp"+str(score))
    if pp==0 and gp==0 and ep==0 and sp==0 and cp==0:
        print("nothing, better luck nextime")
    print()
    print("you have ",end="")
    if tpp>0:
        print("Pp",str(tpp),end=" ")
    if tgp>0:
        print("Gp"+str(tgp),end=" ")
    if tep>0:
        print("Ep"+str(tep),end=" ")
    if tsp>0:
        print("Sp"+str(tsp),end=" ")
    if tcp>0:
        print("Cp"+str(tscore))
    if tpp<=0 and tgp<=0 and tep<=0 and tsp<=0 and tcp<=0:
        print("no coins")
    print()
    tscore=tscore+tsp*10+tep*50+tgp*100+tpp*1000
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
    ppp=math.floor(price/1000)
    price=price-ppp*1000
    pgp=math.floor(price/100)
    price=price-pgp*100
    pep=math.floor(price/50)
    price=price-pep*50
    psp=math.floor(price/10)
    price=price-psp*10
    print("price to go again is ",end="")
    if ppp>0:
        print("Pp",str(ppp),end=" ")
    if pgp>0:
        print("Gp"+str(pgp),end=" ")
    if pep>0:
        print("Ep"+str(pep),end=" ")
    if psp>0:
        print("Sp"+str(psp),end=" ")
    if pcp>0:
        print("Cp"+str(price))
    if tscore>10:
        price=int((1*10**math.log(tscore,10))/2)
    else:
        price=10
    aga=input("would you like to go again (Y/any key): ")
print("you'r score is Gp",str(tscore/100))
