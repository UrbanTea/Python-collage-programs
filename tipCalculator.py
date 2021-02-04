#J Muprhy
#January 24 2021
#the program asks for the survers name, the bill, and the tip persent, then it displays the severs name,
# the origonal bill, the tip amount, then the total amount, fallowed by a visual represnetation of the bill
import math
import time
print("""

████████╗██╗██████╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
╚══██╔══╝██║██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ██║██████╔╝    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
   ██║   ██║██╔═══╝     ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
   ██║   ██║██║         ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═╝   ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝""")
print("""
==========================================================================================================
\n\n""")
name=input("Server's Name: ")
bill=float(input("Check Amount in USD $: "))
tip=int(input("Tip Percent: "))

print("""
==========================================================================================================
\n""")
print("Server's Name:",name)
print("Original Bill:",round(bill,2))
print("Tip Amount:",round(bill*(tip/100),2))
print("\nTotal Amount:",round(bill+round(bill*(tip/100),2),2))


bill=round(bill+round(bill*(tip/100),2),2)
hundred=math.floor(bill/100)
#print("hundred:",hundred,bill)
bill=bill-hundred*100
fifty=math.floor(bill/50)
#print("fifty:",fifty,bill)
bill=bill-fifty*50
ten=math.floor(bill/10)
#print("ten:",ten,bill)
bill=bill-ten*10
five=math.floor(bill/5)
#print("five:",five,bill)
bill=bill-five*5
one=math.floor(bill)
#print("one:",one,bill)
bill=bill-one
qurt=math.floor(bill/.25)
#print("qurt:",qurt,bill)
bill=bill-(qurt/10)
dime=math.floor(bill/.10)
#print("dime:",dime,bill)
bill=bill-(dime/10)
nick=math.floor(bill/.05)
#print("nick:",nick,bill)
bill=bill-(nick/10)
peny=math.floor(bill/.01)
#print("penny:",peny,bill)
bill=bill-(peny/10)

if(hundred>0):
    print("[̲̅$̲̅(̲̅100̲̅)̲̅$̲̅]"*hundred)
if(fifty>0):
    print("[̲̅$̲̅(̲̅50̅)̲̅$̲̅]"*fifty)
if(ten>0):
    print("[̲̅$̲̅(̲̅10̅)̲̅$̲̅]"*ten)
if(five>0):
    print("[̲̅$̲̅(̲̅5̅)̲̅$̲̅]"*five)
if(one>0):
    print("[̲̅$̲̅(̲̅1̲̅)̲̅$̲̅]"*one)
if(dime>0):
    for i in range(0,dime):
        print("(̲̲̅̅)10")
if(peny>0):
    for i in range(0,peny):
        print("(̲̲̲̅̅̅)1")
if(nick>0):
    for i in range(0,nick):
        print("(̲̲̲̲̅̅̅̅)5")
if(qurt>0):
    for i in range(0,qurt):
        print("(̲̲̲̲̲̲̅̅̅̅̅̅)25")


#[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]
