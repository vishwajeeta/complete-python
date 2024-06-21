#can't access element by index
#creating a empty set
set1=set()

#it doesn't repeat same element
set1={1,2,3,3,2,1,4,5,6,7,6,5}
print(set1)

#adding a element
set1.add(10),set1.add(50)
print(set1)

#clear set data
set1.clear()
set1.add(10)
print(set1)


set1 = {10,50,60,30,40}

#type convertion set -> list
omg=list(set1)


#methods:-
# len()
# .remove()
# .pop() -- it would remove a random element
print(omg)


#union --get the value of both set's
a={3,9,7,5,2}
b={3,4,7,1,2}
print(b.union(a))

#intersection --get common values
print(b.intersection(a))

#difference --get non-common values
print(b.difference(a))

sample={1,3,4,"hii"}
print(sample)