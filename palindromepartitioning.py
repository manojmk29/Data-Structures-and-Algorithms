from typing import DefaultDict


class Solution(object):
    def partition(self, word):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        arr=[]
        k=1
        while(k<=len(word)):
            i=0
            while(i<=len(word)-k):
                temp=word[i:i+k]
                if(temp==temp[::-1]):
                    arr.append([i,i+k])
                i+=1
            k+=1
        arr.sort()
        hmap=DefaultDict(list)
        for i in arr:
            hmap[i[0]].append(i[1])
        ans=[]
        def backtrack(pos,hmap,temp):
            if(pos>=len(word)):
                ans.append(temp[:])
                return
            for i in hmap[pos]:
                temp.append(word[pos:i])
                backtrack(i,hmap,temp)
                temp.pop()
        backtrack(0,hmap,[])
        return(ans)