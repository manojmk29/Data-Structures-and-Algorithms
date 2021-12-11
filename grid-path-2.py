def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[ [ -1 for i in range(m) ] for j in range(n) ]
        count=helper(m,n,0,0,dp)
        # return(count)
        return(dp[m][n])

def helper(m,n,i,j,dp):
    if(i==m-1 and j==n-1):
        return(1)
    elif(i>=m or j>=n):
        return(0)
    elif(dp[i][j]!=-1):
        return(dp[m][n])
    else:
        # dp[i][j]=helper(m,n,i+1,j,dp)+helper(m,n,i,j+1,dp)
        return(dp[i][j]=helper(m,n,i+1,j,dp)+helper(m,n,i,j+1,dp))

m=7
n=3
print(uniquePaths(m,n))