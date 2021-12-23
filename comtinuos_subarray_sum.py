class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        #method 1 
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if(sum%k==0):
        #             return(True)
        # return(False)
a =Solution()
nums=[23,2,6,4,7]
k=6
print(a.checkSubarraySum(nums,k))