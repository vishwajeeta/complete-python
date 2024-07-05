'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(n=1+2+3+4+5+...+n)

'''

def sumofn(n):
    if(n==1):
        return 1
    
    return sumofn(n-1)+n
    
a=sumofn(101)
print(a)