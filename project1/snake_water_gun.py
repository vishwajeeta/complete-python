import random
'''
snake water gun game
1=snake
-1=water
0=gun
'''
computer=random.choice([-1,1,0])
youstr =input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"Gun"}

you=youDict[youstr]

print(f"you chose {reverseDict[you]} \ncomputer chose {reverseDict[computer]}")
if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you win")

    elif(computer ==-1 and you==0):
        print("you loose!")

    elif(computer ==1 and you==-1):
        print("you loose!")

    elif(computer ==1 and you==0):
        print("you win!")

    elif(computer ==0 and you==-1):
        print("you win!")

    elif(computer ==0 and you==1):
        print("you loose!")

    else:
        print("someting went wrong!")