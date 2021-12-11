def grid_path(m,n):
    count=helper(m,n,0,0)
    return count

def helper(m,n,i,j):
    if(i==m-1 and j==n-1):
        return(1)
    elif(i>=m or j>=n):
        return(0)
    else:
        return(helper(m,n,i+1,j)+helper(m,n,i,j+1))

m=23
n=12
print(grid_path(m,n))