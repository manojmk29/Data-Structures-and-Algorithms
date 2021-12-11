def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #solution 3
        
        ret=[[1]]
        for i in range(1,numRows):
            ret+=[list(map(lambda a,b:a+b,[0]+ret[i-1],ret[i-1]+[0]))]
        return ret
    
        #solution 2
        
#         ret=[[1]]
#         for i in range(1,numRows):
#             temp1=[0]+ret[-1]
#             temp2=ret[-1]+[0]
#             a=[]
#             for j in range(len(temp1)):
#                 a+=[temp1[j]+temp2[j]]
#             ret+=[a]
#         return ret
                
        #soultion 1
        
#         ret=[None]*numRows
#         for i in range(numRows):
#             ret[i]=[None]*(i+1)
#             ret[i][0]=ret[i][i]=1
#             for j in range(1,i):
#                 ret[i][j]=ret[i-1][j-1]+ret[i-1][j]
#         return ret