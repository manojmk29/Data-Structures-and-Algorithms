def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kandane's algorithm
        curr_max=nums[0]
        global_max=nums[0]
        for i in range(1,len(nums)):
            curr_max=max(nums[i],curr_max+nums[i])
            global_max=max(global_max,curr_max)
        return global_max
        
        
        
#         max_so_far =nums[0]
#         curr_max = nums[0]
     
#         for i in range(1,len(nums)):
#             curr_max = max(nums[i], curr_max + nums[i])
#             max_so_far = max(max_so_far,curr_max)
         
#         return max_so_far
        
        #method 1 o(n^2)
        
        # total=nums[0]
        # for i in range(0,len(nums)):
        #     t=0
        #     for j in range(i,len(nums)):
        #         t+=nums[j]
        #         total=max(t,total)
        # return total