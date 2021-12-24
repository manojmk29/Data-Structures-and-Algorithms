class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        self.backtrack(candidates,ans,target,[])
        return(ans)
    def backtrack(self,candy,ans,target,temp):
        if(target==0):
            ans.extend([temp])
        elif(target<0):
            return
        else:
            for i in range(len(candy)):
                self.backtrack(candy[i:],ans,target-candy[i],temp+[candy[i]])
x=Solution()
arr=[2,7,6,3,5,1]
target=9
anss=x.combinationSum(arr,target)
print(anss)
sam=[[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2],[1,1,1,1,1,1,3],[1,1,1,1,1,2,2],[1,1,1,1,2,3],[1,1,1,1,5],[1,1,1,2,2,2],[1,1,1,3,3],[1,1,1,6],[1,1,2,2,3],[1,1,2,5],[1,1,7],[1,2,2,2,2],[1,2,3,3],[1,2,6],[1,3,5],[2,2,2,3],[2,2,5],[2,7],[3,3,3],[3,6]]
print(sam.sort()==anss.sort())