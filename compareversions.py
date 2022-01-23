class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i=0
        j=0
        it=0
        jt=0
        ie=0
        je=0
        f1=0
        f2=0
        while(i<=len(version1) or j<=len(version2)):
            if((f1!=1) and i>len(version1)):
                ie=i
                f1=1
            elif((f1==0) and (i==len(version1)) or (version1[i]==".")):
                ie=i-1
                f1=1
            elif(f1==0):
                i+=1
            if((f2!=1) and j>len(version2)):
                je=j
                f1=1
            elif((f2==0) and (j==len(version2)) or (version2[j]==".")):
                je=j-1
                f2=1
            elif(f2==0):
                j+=1
            if((f1==1) and (f2==1)):
                if(i>len(version1)):
                        v1=0
                else:
                    v1=int(version1[it:ie+1])
                if(j>len(version2)):
                        v2=0
                else:
                    v2=int(version2[jt:je+1])
                if(v1>v2):
                    return(1)
                elif(v2>v1):
                    return(-1)
                else:
                    it=ie+2
                    jt=je+2
                    if(i<len(version1)):
                        f1=0
                    if(j<len(version2)):
                        f2=0
        return(0)
a=Solution()
print(a.compareVersion("1.01","1.001"))