def mergesort(arr,l,r):
    if(r>l):
        conv=0
        mid=(l+r)//2
        conv+=mergesort(arr,l,mid)
        conv+=mergesort(arr,mid+1,r)
        conv+=merge(arr,l,r,mid)
        return conv
    return(0)
def merge(arr,l,r,mid):
    conv=0
    rr=mid+1
    lt=l
    rt=r
    temp=[]
    while(l<=mid and rr<=r):
        if(arr[l]<arr[rr]):
            temp+=[arr[l]]
            l+=1
        else:
            temp+=[arr[rr]]
            rr+=1
            conv=conv+(mid+1-l)
    while(l<=mid):
        temp+=[arr[l]]
        l+=1
    while(rr<=r):
        temp+=[arr[rr]]
        rr+=1
    for i in range(lt,rt+1):
        arr[i]=temp[i-lt]    
    return conv
arr=[3,2,1]
aa=mergesort(arr,0,len(arr)-1)
print(aa)
