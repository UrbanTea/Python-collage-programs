em=[]

while 1==1:
    x=input("[A] add to the list\n[V] view the list\n[R] Remove from the list\n[E] exit the program\n\n")
    if len(em)<10:
        if x == 'a' or x== 'A':

            emt=input("please input a email\n")
            
            if emt.find("@")>-1 and len(emt)-emt.index(".")==4:
                em.append(emt)
                print(emt,"has been added")
                print(10-len(em),"slots left")
            else:
                print("error")
    else:
        print("list is full")
    if x=='r' or x=='R':
        z=1
        for i in em:
            print(z,em[z-1])
            z=z+1
        y=int(input("please put in a number\n"))
        if y>=1 and y<=len(em)+1:
            print(em[y-1],"removed")
            em.remove(em[y-1])
            

    if x== 'v' or x=='V':
        print(len(em),"/10")
        print(em)


    if x=='e' or x=='E':
        break
    x=""
        
