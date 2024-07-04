#sample function
def wish():
    print("good day")

wish()

#function with argument

def wish(name):
    print(f"good day , {name}")

wish("Alex")


#functions with default arguments | parameter

def wish(name="sir"):
    print(f"good day , {name}")

wish()
wish("iron man")
