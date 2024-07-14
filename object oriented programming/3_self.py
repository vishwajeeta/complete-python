class Employee:
    language = "python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


harry = Employee()
harry.language = "javascript" # This is an instance attribute

# Employee.getInfo(harry)
# or 
harry.getInfo()