#J Murphy
#19/02/2012
#program make a random number between 0-100 and has player guess, then has the computer guess based on a binary search algroithum
import random

beg=0
end=100
x=random.randrange(int(end))
while(beg<=end):
    pg=int(input("player's Guess: "))
    if pg==x:
        print("player is Correct\nYOU WIN")
        break
    elif pg>x:
        print("player is High")
    else:
        print("player is low")
    mid=round((beg+end)/2)
    print("Computer guessed",mid)
    if mid ==x:
        print("Computer is Correct\nGAMEOVER")
        break
    if mid <= x:
        beg = mid+1
        print("Computer is Low")
    else:
        end=mid-1
        print("Computer is High")

            
   
    
