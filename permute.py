class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        n=len(nums)
        def helper(nums,path):
            if(len(path)==n):
                ret.append(path[:])
                return
            for i in nums:
                temp=[ik for ik in nums if(ik!=i)]
                helper(temp,path+[i])
        helper(nums,[])
        return(ret)