li=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----",".-.-.-","--..--"]
que=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.',',']

import subprocess
subprocess.call(["clear"])
print("Morse Code\n----------")
for w in range(1,39):
    help=li[w-1]
    helpo=(15-len(str(help)))
    print(f"{que[w-1]} : {help}",end=helpo*" ")
    if(w%4!=0):
        continue
    else:
        print("\n")
st=input('\n\nPress "S" to start the practise : ')
if(st=='S'):
    subprocess.call(["clear"])
    check=1
    while(check):
        try:
            check=0
            p=int(input("How many times do you wish to play : "))
        except ValueError:
            check=1
            print("\nForbidden, enter a number🔄...\n")
    if(p>0):
        ch=input("\n\n\n1) Alphabets\n2) Numbers\n3) AlphaNumeric\n\nEnter your choice : ")
        print("\n-----------------------------------\n")
        gp=input("1) Morse to Characters\n2) Characters to Morse\n\nEnter gameplay : ")
        subprocess.call(["clear"])
        from random import randint
        t,c,w=0,0,0
        for i in range(p):
            if ch=='1':
                le=randint(0,25)
            elif ch=='2':
                le=randint(26,35)
            elif ch=='3':
                le=randint(0,37)
            else:
                print("Invalid")
            t=t+1
            if gp=='2':
                print(f"{i+1}) {que[le]}")
                an=li[le]
                inp=input("Morse : ")
            elif gp=='1':
                print(f"{i+1}) {li[le]}")
                an=que[le]
                inp=input("Character : ")
            if inp==an:
                print("Correct :)\n")
                c+=1
                #print(c,"/",t,"\n")
            else:
                print("Wrong :(")
                print("Answer :",an,"\n")
                w+=1
                #print(w,"/",t,"\n")
        ac=round(c/t*100,2)
        ro=6*" "
        to=(8-len(str(t)))*" "
        co=(8-len(str(c)))*" "
        wo=(8-len(str(w)))*" "
        aco=(7-len(str(ac)))*" "
        print(f"\n+--------------------+\n| {ro}Result {ro}|\n+--------------------+\n| Total    : {t}{to}|\n| Correct  : {c}{co}|\n| Wrong    : {w}{wo}|\n| Accuracy : {ac}%{aco}|\n+--------------------+")
        if(ac==100):
            print("\nWell done buddy...!🎉\n")
        elif(ac>=80):
            print("\nAlmost there...!↗️\n")
        elif(ac<80):
            print("\nKeep hustling buddy, long way to go🏃‍♂️\n")
        #print(f"Result\n-----------------\nTotal    : {t}\nCorrect  : {c}\nWrong    : {w}\nAccuracy : {ac}%")
    else:
        print("\nFeeling sad to see you go without trying.🥺\nGood Bye...!🙏\n")
else:
    print("\nWrong key, Exited☑️\n")