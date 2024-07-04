# Recurstion is a function which calls itself
# Note:-
''' 
maximum rectusion in python is 998 times, int

float value will cause error as
 "maximum recursion depth exceeded in comparison"


'''

#Example of factorial

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
        

print(factorial(90))
