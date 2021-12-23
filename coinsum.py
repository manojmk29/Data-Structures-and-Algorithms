def coinsum(arr,val):
    arr.sort(reverse=True)
    count=0
    for i in range(len(arr)):
        if(arr[i]<=val):
            count+=val//arr[i]
            val=val%arr[i]
    return(count)
arr=[10,5,50,1,2]
v=123
print(coinsum(arr,v))
