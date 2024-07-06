import random
computer=random.choices([1,2,3,4,5,6])
you=int(input("Enter your choice: "))
if(you>=6 or you<=0):
    print("pleace choose above 0 and below 7")
else:
    if(computer==you):
        print("You win")
    else:
        print("you lose!")