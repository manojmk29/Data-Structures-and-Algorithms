class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret=[]
        start=0
        end=k
        while(end<=len(nums)):
            temp=nums[start]
            for i in range(start+1,end):
                temp=max(temp,nums[i])
            start+=1
            end+=1
            ret.append(temp)
        return(ret)