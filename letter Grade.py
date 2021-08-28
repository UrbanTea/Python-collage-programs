#J Murphy
#07/02/2021
#the program takes an input of the max Score posable, then takes an input of the Score gained, then ouputs a letter grade

ma=int(input("max possable Score: "))
cu=int(input("Score: "))
p=100*(cu/ma)
print(str(round(p,2))+"%")
def letterGrade(x,y,l):
    if p>=x and p<=y:
        print(l)

if p>100:
    print("error score is greater than max score")

letterGrade(97,100,"A+")
letterGrade(93,96,"A")
letterGrade(90,92,"A-")
letterGrade(87,89,"B+")
letterGrade(83,86,"B")
letterGrade(80,82,"B-")
letterGrade(77,79,"C+")
letterGrade(73,76,"C")
letterGrade(70,72,"C-")
letterGrade(67,69,"D+")
letterGrade(65,66,"D")
letterGrade(0,64,"F")
if p<0:
    print("error score percent is negitave")
