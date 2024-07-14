class Employee:
    
    language="python" #This is a class attribute
    LPA=1200000

data=Employee()
data.language="javascript" # This is an instance attribute
# instance attributes,take preferance over class attributes during assignment & retrival
print(data.language,data.LPA)

print(type(data.language))
print(type(data))
print(type(Employee))