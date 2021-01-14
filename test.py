#number=input("please input a size:")
import time
for number in range(1,100,1):
    if int(number)>1:
        print("*"*int(number))
        for i in range(1,int(number)-1,1):
            print("*"," "*int(int(number)-4),"*")
        print("*"*int(number))   
    if int(number)<1:
        print("Error minmum number is 1")
    if int(number)==1:
        print("*")
    print(number)
    time.sleep(.2)
