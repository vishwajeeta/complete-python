dist1={
    "aman":98,
    "ajay":77,
    "nikil":80,
    0:"hii"
}

#get list of key value pairs in tuple form
print(dist1.items())
print(dist1)
print(dist1["ajay"])

# get keys of a list
print(dist1.keys())
# get values of a list
print(dist1.values())

# updating
print("updating disctionaly of aman and adding new key:value rahul")
dist1.update({"aman":0,"rahul":98})
print(dist1)

# error free way to fetch elements
print("ajay is =",dist1.get("ajay"))
