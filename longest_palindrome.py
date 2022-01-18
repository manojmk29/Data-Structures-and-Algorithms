class Solutions():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=s[0]
        mat=1
        for i in range(len(s)):
            l=i
            r=i
            while(True):
                if(l>0 and r<len(s)-1 and s[l-1]==s[r+1]):
                    l-=1
                    r+=1
                    le=r-l+1
                    if(le>mat):
                        mat=le
                        ret=s[l:r+1]
                elif(l==r and r<len(s)-1 and s[r+1]==s[r]):
                    r+=1
                    le=r-l+1
                    if(le>mat):
                        mat=le
                        ret=s[l:r+1]
                elif(l==r and l>0 and s[l-1]==s[l]):
                    l-=1
                    le=r-l+1
                    if(le>mat):
                        mat=le
                        ret=s[l:r+1]
                else:
                    break
        return(ret)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                if(temp==temp[::-1] and (len(temp)>len(ret))):
                    ret=temp
        return(ret)
class Solution2():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=s[0]
        mat=1
        def helper(l,r):
            while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
                l-=1
                r+=1
            return(l+1,r-1)
        for i in range(len(s)):
            l1,r1=helper(i,i)
            le1=r1-l1+1
            if(i>0 and s[i-1]==s[i]):
                l2,r2=helper(i-1,i)
                le2=r2-l2+1
            else:
                le2=-1
            if(le1>le2 and le1>mat):
                mat=le1
                ret=s[l1:r1+1]
            elif(le2>=le1 and le2>mat):
                mat=le2
                ret=s[l2:r2+1]
        return(ret)
o=Solution2()
print(o.longestPalindrome("bb"))