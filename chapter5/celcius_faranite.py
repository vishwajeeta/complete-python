#formula [ c/5=(f-32)/9 ]

def F_to_c(f1):
    return 5*(f1-32)/9
f1 = int(input("Enter temprature in F:"))
print(F_to_c(f1))
print(round(F_to_c(f1),2)) #get only 2 decimal places