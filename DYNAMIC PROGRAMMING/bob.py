def solve(n,x,a):
    def helper(ind,tot,cnt):
        if ind==n:
            for i in range(cnt,-cnt-1,-1):
                val=tot+i
                if (val%x==0):
                    return(val)
            return(-float("inf"))
        l=helper(ind+1,tot+a[ind],cnt+1)
        r=helper(ind+1,tot,cnt)
        return max(l,r)
    return(helper(0,0,0))         

ans=solve(5,4,[4,8,6,2,1])
print("ans=====",ans)