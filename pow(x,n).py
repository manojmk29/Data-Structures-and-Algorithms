def pow(x,n):
    if(n<0):
        n*=-1
        x=1/x
    if(n==0):
        return(1)
    if(n==1):
        return(x)
    if(n%2==0):
        return(pow(x*x,n//2))
    else:
        return((pow(x,n-1)*x))
x=2
n=-10
print(pow(x,n))