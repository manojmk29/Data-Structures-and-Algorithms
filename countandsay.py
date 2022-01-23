class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(inp):
            if(inp==1):
                return("1")
            ans=helper(inp-1)
            ret=""
            val=ans[0]
            count=1
            for i in ans[1:]:
                if(val==i):
                    count+=1
                else:
                    ret=ret+str(count)+i
                    val=i
                    count=1
            ret=ret+str(count)+ans[-1]
            return(ret)
        return helper(n)
a=Solution()
print(a.countAndSay(4))