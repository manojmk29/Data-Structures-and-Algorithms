
# method 1 tle
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def helper(ind,miv,count):
            if(ind==len(heights)):
                return
            value=heights[ind]
            if(value==miv):
                count+=1
                ret[0]=max(ret[0],(count*miv))
                helper(ind+1,miv,count)
            elif(value>miv):
                count+=1
                val=max(value,(count*miv))
                ret[0]=max(ret[0],val)
                helper(ind+1,miv,count)
                helper(ind+1,value,1)
            elif(value<miv):
                helper(ind+1,value,1)
        def helper_rev(ind,miv,count):
            if(ind==-1):
                return
            value=heights[ind]
            if(value==miv):
                count+=1
                ret[0]=max(ret[0],(count*miv))
                helper_rev(ind-1,miv,count)
            elif(value>miv):
                count+=1
                val=max(value,(count*miv))
                ret[0]=max(ret[0],val)
                helper_rev(ind-1,miv,count)
                helper_rev(ind-1,value,1)
            elif(value<miv):
                helper_rev(ind-1,value,1)
        for i in 
        ret=[heights[0]]
        miv=heights[0]
        ind=1
        count=1
        helper(ind,miv,count)
        miv=heights[-1]
        ind=len(heights)-2
        count=1
        helper_rev(ind,miv,count)
        return(ret[0])
o=Solution()
arr=[2,1,5,6,2,3,1,1,1,1,1]
print(o.largestRectangleArea(arr))