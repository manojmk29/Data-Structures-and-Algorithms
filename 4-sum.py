def fourSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        #method 1 O(n^4)
        # output=[]
        # n=len(nums)
        # nums.sort()
        # for i in range(0,n-3):
        #     for j in range(i+1,n-2):
        #         for k in range(j+1,n-1):
        #             for l in range(k+1,n):
        #                 if(nums[i]+nums[j]+nums[k]+nums[l]==target):
        #                     sample=[nums[i],nums[j],nums[k],nums[l]]
        #                     if(sample not in output):
        #                         output+=[sample]
        #                     # output+=[[nums[i],nums[j],nums[k],nums[l]]]
        # return(output)
        #method 2
        output=[]
        n=len(nums)
        nums.sort()
        def binary_search(i,j,k,l,r,target,output):
             while(l<=r):
                m=(l+r)//2
                if(nums[i]+nums[j]+nums[k]+nums[m]==target):
                    output+=[[nums[i],nums[j],nums[k],nums[m]]]
                    # if([nums[i],nums[j],nums[k],nums[m]] not in output):
                    #     output+=[[nums[i],nums[j],nums[k],nums[m]]]
                    #     break
                elif(nums[i]+nums[j]+nums[k]+nums[m]>target):
                    r=m-1
                elif(nums[i]+nums[j]+nums[k]+nums[m]<target):
                    l=m+1
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                        binary_search(i,j,k,k+1,n-1,target,output)
        return(output)
nums=[-5,5,4,-3,0,0,4,-2]
tar=4
print(fourSum(nums,tar))