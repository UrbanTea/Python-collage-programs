#J Muprhy
#January 13 2021
#Program prints a box of *  at the size of the inputed number
number=input("please input a size:")

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
    
