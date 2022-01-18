class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        ret=0
        while(i<len(height)):
            j=i+1
            maxi=j
            maxsumt=0
            maxcount=0
            sumt=0
            count=0
            while(j<len(height)):
                if(height[j]>=height[i]):
                    maxi=j
                    maxsumt=sumt
                    maxcount=count
                    break
                if(height[j]>height[maxi]):
                    maxi=j
                    maxsumt=sumt
                    maxcount=count
                sumt+=height[j]
                count+=1
                j+=1
            if((count==0)):
                i+=1
            else:
                mint=min(height[i],height[maxi])
                val=(maxcount*mint)-maxsumt
                ret+=val  
                i=maxi
        return(ret)
o=Solution()
print(o.trap([4,2,3]))