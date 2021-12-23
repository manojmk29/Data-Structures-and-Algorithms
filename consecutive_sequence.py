class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table=set()
        res=1
        def find(i):
            if i in table:
                table.remove(i)
                return(1+find(i-1)+find(i+1))
            return(0)
        for i in nums:
            table.add(i)
        for i in nums:
            temp=find(i)
            res=max(temp,res)
        return(res)
obj=Solution()
arr=[1,2,3,4,9,8,7,30,40]
out=obj.longestConsecutive(arr)
print(out)