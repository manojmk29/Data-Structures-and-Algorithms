def mergesort(arr,l,r):
    if(r>l):
        mid=(l+r)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)
        merge(arr,l,r,mid)
def merge(arr,l,r,mid):
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
    while(l<=mid):
        temp+=[arr[l]]
        l+=1
    while(rr<=r):
        temp+=[arr[rr]]
        rr+=1
    for i in range(lt,rt+1):
        arr[i]=temp[i-lt]    
arr=[3,2,5,7,1,2,10,-4]
mergesort(arr,0,len(arr)-1)
print(arr)