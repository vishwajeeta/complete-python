class Employee:
    
    language="python" #This is a class attribute
    LPA=1200000


#creating a object

print(Employee.language)
print(Employee.LPA)

#creating a object
obj1=Employee.language
print(obj1)

obj2=Employee

# language and LPA are class atttributes
print(obj2.language,obj2.LPA)

#printing additional value
obj2.name="vishwa" #this is an object attribute/instance attribute
print(obj2.name,obj2.language,obj2.LPA)
#here name is object/instance attribute and salary,LPA is class attributes as they directly belong to the class