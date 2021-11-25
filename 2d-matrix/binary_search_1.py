def binary_search_helper(arr,r,c_min,c_max,x):
    while(c_min<=c_max):
        c_mid=(c_min+c_max)//2
        if(arr[r][c_mid]==x):
            return([r,c_mid])
        elif(arr[r][c_mid]>x):
            c_max=c_mid-1
        elif(arr[r][c_mid]<x):
            c_min=c_mid+1
    return(-1)

def binary_search(arr,n,m,x):
    if(n==1):
        return(binary_search_helper(arr,0,0,m-1,x))
    r_min=0
    r_max=n-1
    c_min=0
    c_max=m-1
    c_mid=(c_min+c_max)//2
    while(r_min+1<r_max):
        r_mid=(r_min+r_max)//2
        if(arr[r_mid][c_mid]==x):
            return([r_mid,c_mid])
        elif(arr[r_mid][c_mid]<x):
            r_min=r_mid
        elif(arr[r_mid][c_mid]>x):
            r_max=r_mid
    if(arr[r_min][c_mid]==x):
        return([r_min,c_mid])
    elif(arr[r_max][c_mid]==x):
        return([r_max,c_mid])
    elif(x<arr[r_min][c_mid]):
        return(binary_search_helper(arr,r_min,0,c_mid-1,x))
    elif(x>arr[r_max][c_mid]):
        return(binary_search_helper(arr,r_max,c_mid+1,m-1,x)) 
    elif((x>arr[r_min][c_mid]) and (x<=arr[r_min][m-1])):
         return(binary_search_helper(arr,r_min,c_mid+1,m-1,x))
    elif((x<arr[r_max][c_mid]) and (x>=arr[r_max][0])):
         return(binary_search_helper(arr,r_max,0,c_mid-1,x))

arr=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# arr=[[1,2,3]]
n=len(arr)
m=len(arr[0])
x=9
print(binary_search(arr,n,m,x))