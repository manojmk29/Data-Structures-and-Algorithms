def sortColors(nums):
        #method 2
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1  
        
        #method 1 
        
        # dic={}
        # dic[0]=0
        # dic[1]=0
        # dic[2]=0
        # for i in nums:
        #         dic[i]+=1
        # j=0
        # for i in range(dic[0]):
        #     nums[j]=0
        #     j+=1
        # for i in range(dic[1]):
        #     nums[j]=1
        #     j+=1
        # for i in range(dic[2]):
        #     nums[j]=2
        #     j+=1
        