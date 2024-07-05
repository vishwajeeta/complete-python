def star(n):
    if(n==0):
        return "*"
    print("*"*n)
    star(n-1)
    

star(20)


def star1(n,i=0):
    if(n<=0):
        return "*"
    i+=1
    print("*"*i)
    
    return star1(n-1,i)

    
star1(10)

