## Read and Write Binary file
```python
#Reading binary file
f=open("image1.jpg","rb")
data=f.read()
print(data)
f.close()

#Writing binary file (b+w read and write)
f=open("image2.jpg","b+w")
data=f.write(data)
print(data)
f.close()
```