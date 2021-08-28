#J murphy
#01/03/2012
#the program pick and random word then asks the player to eather guess the word or letter in the word
import random
title="Guess the Word Game"
#word=("test","python","mark","map","apple")
with open('Guess the word game words.txt','r') as f:
    word=f.readlines()
    for i in range(len(word)):
        word[i].replace('\n','')
#print(word)
rand=random.randrange(len(word))
x=""
y=""
z=""
for i in word[rand]:
    y=y+i
guesses=[]
guessnum=int(0)
gc=[]
temp=0
a=[]
print(title.center(80,"="))
#print(word[rand])
for i in word[rand]:
    #print("*",end="")
    temp=temp+1
    z=z+"*"
    x=x+"*"
    #print(x)
temp=0

print(x.center(80))
#print(len(word[rand]))
x=""
responce ="n"
while responce.lower() != "y":
    responce = input("would you like to guess the word (y/n): ")
    if responce.lower() != "n" and responce.lower() != "y":
        print("Error wrong input")
        continue
    if responce.lower() == "y":
        break
    guesses.insert(guessnum,input("Please input a Chariture: "))
    for i in word[rand]:
        if guesses[guessnum].upper()==i:
            temp=temp+1
    
    gc.insert(guessnum,int(temp))
    temp=0
    for i in range(len(word[rand])):
        #print(i,end="")
        if guesses[guessnum].upper()== y[i]:
            x=x+guesses[guessnum].lower()
        else:
            x=x+z[i]
    
    z=x
    print(x[0:len(x)-1])
    x=""
    print("the letter:",str(guesses[guessnum]),"is in the word ",int(gc[guessnum]),"times")
    print("previous guesses")
    guessnum=guessnum+1
    for i in range(len(guesses)-1):
        print(guesses[i],"=",gc[i])

guess=input("please input the word: ").upper()
guess=guess+"\n"
#guess=guess.lower
print("you guessed",guess)
print("the word is",word[rand])
if guess == word[rand]:
    print("good job")
else:
    print("better luck next time")


