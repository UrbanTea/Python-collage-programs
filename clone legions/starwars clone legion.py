import sys
import random
sc=""
rn=1
bn=1
cn=1
pn=1
nn=0
i=0
x=""
def open_file(file_name, mode):
    try:
        file=open(file_name, mode)
    except IOError as e:
        print("Unable to open file:",str(file_name)+". Is it still there\nEnding program")
        input("\n\nPress enter to exit")
        sys.exit()
    else:
        return file
def generate_numb():
    ct=0
    cm=""
    f=open_file("Clone_numbers.txt","r")
    ct=random.randrange(9999)
    while str(ct) in str(f):
        ct=random.randrange(9999)
    cm=str(ct)
    f.close()
    f=open_file("Clone_numbers.txt","a")
    f.write(cm.zfill(4)+"\n")
    f.close()
    return cm.zfill(4)
for r in range(4):
    for b in range(4):
        for c in range(4):
            for p in range(4):
                for ss in range(4):
                    for s in range(9):
                        i=i+1
print(i)
f=open_file("Clone_numbers.txt","w")
f.write("[=Clone Numbers=]\n")
f.write("7358\n")
f.write("1798\n")
f.write("7342\n")
f.write("7306\n")
f.write("7384\n")
f.close()
f1=open_file("Clone_Leagion.txt","w")
f1.write("[=141st Clone Leagion=]\n")


for r in range(4):
    
    f1.write(str(rn)+" Regiment\n")
    rn=rn+1
    for b in range(4):
        f1.write(str(" "*2)+str(bn)+" Battalion Commander: CC-"+str(generate_numb())+"\n")
        f1.write(str(" "*4)+" Major: CC-"+str(generate_numb())+"\n")
        bn=bn+1
        for c in range(4):
            f1.write(str(" "*6)+str(cn)+" Company captain: CC-"+str(generate_numb())+"\n")
            cn=cn+1
            for p in range(4):
                f1.write(str(" "*8)+str(pn)+" Platoon lieutenant: CL-"+str(generate_numb())+"\n")
                f1.write(str(" "*10)+" Sergeant-major: CT-"+str(generate_numb())+"\n")
                for ss in range(4):
                    if ss==0:
                        sc="Red"
                    elif ss==1:
                        sc="Blue"
                    elif ss==2:
                        sc="Green"
                    elif ss==3:
                        sc="Yellow"
                    f1.write(str(" "*12)+str(pn)+" "+str(sc)+" Squad Sergeant: CT-"+str(generate_numb())+"\n")
                    f1.write(str(" "*14)+str(pn)+" "+str(sc)+" Squad Corporal: CT-"+str(generate_numb())+"\n")
                    for s in range(9):
                        f1.write(str(" "*16)+str(pn)+" "+str(sc)+" Squad Trooper "+str(s+1)+": CT-"+str(generate_numb())+"\n")
                        nn=nn+1
                        print(i-nn,str((nn/i)*100)+"%")
                pn=pn+1
f1.close()
