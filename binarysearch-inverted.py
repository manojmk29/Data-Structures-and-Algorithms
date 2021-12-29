def search(arr,x):
    l=0
    r=len(arr)-1
    while(l<=r):
        m=(l+r)//2
        if(arr[m]==x):
            return(m)
        if((arr[m]>x) and arr[l]<=x):
            r=m-1
        elif((arr[m]>x) and arr[l]>x):
            l=m+1
        elif((arr[m]<x) and arr[r]>=x):
            l=m+1
        elif((arr[m]<x) and arr[r]<x):
            r=m-1
    return(False)
arr=[1,2,3,4,5,6]
x=6
print(search(arr,x))