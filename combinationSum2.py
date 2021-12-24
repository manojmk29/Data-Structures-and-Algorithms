class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans=[]
        self.backtrack(0,candidates,ans,target,[])
        return(ans)
    def backtrack(self,pos,cand,ans,target,path):
        if(pos==len(cand) or target<0):
            if(target==0):
                ans.append(path[:])
            return
        self.backtrack(pos+1,cand,ans,target-cand[pos],path+[cand[pos]])
        pos+=1
        while(pos<len(cand) and cand[pos]==cand[pos-1]):
            pos+=1
        self.backtrack(pos,cand,ans,target,path)
x=Solution()
candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27
print(x.combinationSum2(candidates,target))