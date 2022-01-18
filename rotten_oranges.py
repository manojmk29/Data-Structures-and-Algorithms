class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if(grid[i][j]==1):
                        return(False)
            return(True)
        def make_rot(i,j,queue):
            if((i!=0) and (grid[i-1][j]==1)):
                grid[i-1][j]=2
                queue.append((i-1,j))
            if(i!=len(grid)-1 and grid[i+1][j]==1):
                grid[i+1][j]=2
                queue.append((i+1,j))
            if(j!=0 and grid[i][j-1]==1):
                grid[i][j-1]=2
                queue.append((i,j-1))
            if(j!=len(grid[0])-1 and grid[i][j+1]==1):
                grid[i][j+1]=2
                queue.append((i,j+1))
        def helper(queue,time):
            if(len(queue)==0):
                if(check()==True):
                    return(time-1)
                else:
                    return(-1)
            next_queue=[]
            for i in queue:
                make_rot(i[0],i[1],next_queue)
            return(helper(next_queue,time+1))
        queue=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    queue.append((i,j))
        return(helper(queue,0))
o=Solution()
a=o.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(a)