#J.Murphy
#15/02/2012
#program flips a coin, and says the result, then taleys up the total
import random
ht=True
h=int(0)
t=int(0)
for i in range(0,100):
    ht=bool(random.getrandbits(1))
    if ht==True:
        h+=1
        print("heads",h+t)
    if ht==False:
        t+=1
        print("tails",h+t)
print("H:"+"|"*h,h)
print("T:"+"|"*t,t)
