class Solution():
    def subsets(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        first=[]
        n=len(nums)
        def helper(pos,arr):
            if(pos==n):
                ans.append(arr[:])
                return
            helper(pos+1,arr[:])
            arr+=[nums[pos]]
            helper(pos+1,arr[:])
        helper(0,first)
        return(ans)
o=Solution()
print(o.subsets([1,2,3]))