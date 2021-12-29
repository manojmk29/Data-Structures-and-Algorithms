class Solution:
    	def NthRoot(self, n, m):
            l=1
            r=m//n
            while(l<=r):
                mid=(l+r)//2
                ans=1
                for i in range(n):
                    ans*=mid
                if(ans==m):
                    return(mid)
                elif(ans>m):
                    r=mid-1
                else:
                    l=mid+1
            return(-1)
o=Solution()
o.NthRoot(1,4)