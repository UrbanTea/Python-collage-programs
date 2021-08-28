#J Murphy
#28/04/2012
#this program takes two inputed numbers and multiplies them then tells the use if the number is greater, less than, or equal to 10
def program1():
    print("program 1")
    print("\n\n")
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    num3=num1*num2
    print("num1 *num2 =",num3)
    print("numb3 is",end=" ")
    if num3>10:
        print("greater than",end=" ")
    elif num3==10:
        print("equal to",end=" ")
    else:
        print("less than",end=" ")
    print("10")
    input("press enter to continue")
#this program counts from 100 to 0 by 2
def program2():
    for i in range(0,100,2):
        print(100-i,end=',')
    print("0")
    input("press enter to continue")
#this program takes the word vareiable and replaces all the constinants with *'s then prints the word then the result
def program3():
    word="incomprehensibilities"
    vouls="aeiou"
    result=""
    for i in word:
        if i in vouls:
            result+=i
        else:
            result+="*"
    print(word)
    print(result)
    input("press enter to continue")
#this program first asks the user to add a item to the zoo_list then it displays all the items in the list with the letter "e" in them, then it prints the first item then removes it, next it prints the number of items in the list, and lastly prints all the items left in the list

def program4():
    zoo_list = ['giraffe', 'parrot', 'python', 'elephant', 'zebra', 'bison']
    print("I am going to visit some animals at the zoo")
    zoo_list.append(input("What should I add to the list? "))
    print("these animals have an \"e\" in there name:")
    for i in zoo_list:
        if "e" in i:
            print(i)
    print("The first animal I will see is the",zoo_list[0])
    zoo_list.remove(zoo_list[0])
    print("I have",len(zoo_list),"anumals left to visit")
    for i in zoo_list:
        print(i)
    input("press enter to continue")
#this program asks for a day of the week and then checks if the item is a day of the week
def program5():
    weekdays=[ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',"sunday"]
    day=input("Input a possible day of the week: ")
    if day.lower() in weekdays:
        print("yes that is a day of the week")
    else:
        print("No, that is NOT a day of the week")
    input("press enter to continue")
program1()
program2()
program3()
program4()
program5()
