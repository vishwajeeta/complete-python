# get 7 fruits names from user and sort them
fruit=[]
i=0
print("Enter frute names")
while i<7:
    
    user=input()
    fruit.append(user)
    i+=1
print(f"Before sorting \t {fruit}")
fruit.sort()

print(f"Before sorting \t {fruit}")


# sum the list
list1=[7,5,2,1,3,4,5,6]
print(list1)

print(f"Sum={sum(list1)}")

# count number of 0 in a tuple
tup1=(1,9,0,2,0,5,3,0,9)
print(f"There are {tup1.count(0)} 0's")