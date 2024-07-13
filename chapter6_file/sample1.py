
#Read the file
f=open("file.txt")
data=f.read()
print(data)
f.close()

#Write the file
f=open("file.txt","w")
data=f.write("hii")
f.close()

#Read line by line
f=open("multiline.txt")
data=f.readlines()
print(data)
print(type(data))
f.close()

#Read a line
f=open("multiline.txt")
#The number of time (n) we will execute the program ,it will run that (n)th line
data1=f.readline()
print(data1)
data2=f.readline()
print(data2)
data3=f.readline()
print(data3)
print(type(data))
f.close()


#Read a line using loop
f=open("multiline.txt")
line=f.readline()
while line !="":
    print(line)
    line=f.readline()
f.close()

# a - open for appending
f=open("file.txt","a")
data=f.write("hii\n")
f.close()


#Reading binary file
f=open("image1.jpg","rb")
data=f.read()

f.close()

#Writing binary file (b+w read and write)
f=open("image2.jpg","b+w")
data=f.write(data)

f.close()



f=open("image1.jpg","rb")
data=f.read()
f.close()

#Writing binary file (b+w read and write)
f=open("image3.png","b+w")
data=f.write(data)
f.close()



f=open("image1.jpg","rb")
data=f.read()
f.close()

f=open("image_row_data.txt","b+w")
data=f.write(data)
f.close()




# a - open for appending
# b - binary file (graphics) only read
# r+w binary file read & write