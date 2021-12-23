class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        t=[]
        for i in range(n):
            t.append((arr[i],dep[i]))
        c=1
        mint=t[0][1]
        for i in range(1,n):
            val=t[i][0]
            if(val<mint):
                c+=1
                mint=min(mint,t[i][1])
            else:
                mint=t[i][1]
        return(c)
a=Solution()
arr=[900,940,950,1100,1500,1800]
dep=[910,1200,1120,1130,1900,2000]
n=6
aa=a.minimumPlatform(n,arr,dep)
print(aa)