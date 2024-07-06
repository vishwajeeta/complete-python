import random

computer=random.choices([1,2,3,4,5,6])
you=int(input("Enter your choice: "))
computer=computer[0]
print(f"computer chosed:{computer}\nyou chosed:{you}")
if(you>6 or you<=0):
    print("pleace choose above 0 and below 7")
else:
    if(computer==you):
        print("congrates You win!")
        print("Password is: ***************** ")
    else:
        print("you lose!")