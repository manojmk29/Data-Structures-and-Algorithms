n=5
def remove_x(pos,arr,x):
    if(pos==len(arr)):
        return([])
    if(arr[pos]!=x):
        return(arr[pos]+remove_x(pos+1,arr[pos:],x))
    else:
        return(remove_x(pos+1,arr,x))
arr=["m","a","n","o","j"]
x="m"
print(remove_x(0,arr,x))