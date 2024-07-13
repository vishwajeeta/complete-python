f=open("file.txt")
data=f.read()
print(data)
f.close()

#Same using with
with open("file.txt") as f:
    print(f.read())
