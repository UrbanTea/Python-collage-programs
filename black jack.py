#J Murphy
#12/04/2021
#this program plays a game of blackjack with the player
import random
numb = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
suit= ("\u2660","\u2663","\u2665","\u2666")
deck=[]
hand=[]
dhand=[]
s=0
ps=0
hs=""
#this creats the deck
def creat_deck():
    for s in range(len(suit)):
        for n in range(len(numb)):
           deck.append((numb[n],suit[s]))

#this adds a card to the hand as long as there are still cards in the deck (there was a annoying bug that would empty out the deck)
def add_hand(i):
    global deck
    if len(deck)>0:
        r=random.randrange(len(deck))
        hand.append(deck[r])
        deck.remove(hand[i])
#this gives the dealer there first card
creat_deck()
add_hand(0)
dhand=hand
hand=[]
print("dealer's card")
print("["+str(dhand[0][0])+str(dhand[0][1])+"]",end="")
print()
print("your hand")
#this scores the hand
def sum_hand():
    global s
    s=0
    al=0
    ah=0
    for i in range(len(hand)):
        if hand[i][0]=="A":
            al=al+1
            ah=ah+11
        elif hand[i][0]=="J" or hand[i][0]=="Q" or hand[i][0]=="K":
            al=al+10
            ah=ah+10
        else:
            al=al+int(hand[i][0])
            ah=ah+int(hand[i][0])
        if ah<21 and al!=ah:
            s=ah
        elif ah>21 and al!=ah:
            s=al
        else:
            s=al
    
#this is for the players turn where the hand reprosents the players hand
for x in range(2):
    add_hand(x)
while s<21:
    for i in range(len(hand)):
        print("["+str(hand[i][0])+str(hand[i][1])+"]",end="")
    print()
    sum_hand()
    if s<21:
        print(s)
        hs=input("Would you like to hit [h] or stand [s]: ")
        if hs=="h" or hs=="H":
            add_hand(len(hand))
        elif hs=="s" or hs=="S":
            break
        else:
            print("Error bad input")
        continue
    elif s>21:
        print("Bust")
#this is for the dealer's turn where the hand reprosents the dealer's hand
if s<=21:
    ps=s
    s=0
    print("dealers hand")
    hand=dhand
    while s<17 and s<=21:
        add_hand(len(hand))
        sum_hand()
        if deck==[]:
            print("error")
            break
    for i in range(len(hand)):
            print("["+str(hand[i][0])+str(hand[i][1])+"]",end="")
    print()
    print(s)
    if s>21:
        print("dealer bust you win")
    elif s==21:
        print("dealer got blackjack you lose")
    elif ps>s:
        print("you win")
    else:
        print("you lose")
#this prints out the deck
for i in range(len(deck)):
    print("["+str(deck[i][0])+str(deck[i][1])+"]",end="")
        


##print("┌─────┐")
##if numb[n]=="10":
##    print("│"+numb[n],"  │")
##else:
##    print("│"+numb[n],"  ","│")
##print("│     │")
##print("│"+" ",suit[s]," │")
##print("│     │")
##if numb[n]=="10":
##    print("│  ",numb[n]+"│")
##else:
##    print("│","  ",numb[n]+"│")
##print("└─────┘")
        
