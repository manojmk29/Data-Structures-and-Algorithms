def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        m=len(matrix[0])
        x=target
        r_min=0
        r_max=n-1
        c_min=0
        c_max=m-1
        c_mid=(c_min+c_max)//2
        if(n==1):
            return(self.binary_search_helper(matrix,0,0,m-1,x))
        while(r_min+1<r_max):
            r_mid=(r_min+r_max)//2
            if(matrix[r_mid][c_mid]==x):
                return(True)
            elif(matrix[r_mid][c_mid]<x):
                r_min=r_mid
            elif(matrix[r_mid][c_mid]>x):
                r_max=r_mid
        if(matrix[r_min][c_mid]==x):
            return(True)
        elif(matrix[r_max][c_mid]==x):
            return(True)
        elif(x<matrix[r_min][c_mid]):
            return(self.binary_search_helper(matrix,r_min,0,c_mid-1,x))
        elif(x>matrix[r_max][c_mid]):
            return(self.binary_search_helper(matrix,r_max,c_mid+1,m-1,x))
        elif((x>matrix[r_min][c_mid]) and (x<=matrix[r_min][m-1])):
             return(self.binary_search_helper(matrix,r_min,c_mid+1,m-1,x))
        elif((x<matrix[r_max][c_mid]) and (x>=matrix[r_max][0])):
             return(self.binary_search_helper(matrix,r_max,0,c_mid-1,x))

def binary_search_helper(self,matrix,r,c_min,c_max,x):
    while(c_min<=c_max):
        c_mid=(c_min+c_max)//2
        if(matrix[r][c_mid]==x):
            return(True)
        elif(matrix[r][c_mid]>x):
            c_max=c_mid-1
        elif(matrix[r][c_mid]<x):
            c_min=c_mid+1
    return(False)