def subsets(nums,res=[[]],pos=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(pos<len(nums)):
            num=nums[pos]
            arr=[]
            for i in res:
                arr.append(i+[num])
            res+=arr
            return(subsets(nums,res,pos+1))
        else:
            return(res)
print(subsets([0]))