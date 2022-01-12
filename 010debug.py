import collections
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        ans=collections.deque([])
        for i in s:
            temp=collections.deque([])
            ind=len(ans)-1
            while((ind>-1) and (ans[ind]<i)):
                    temp.append(ans.pop())
                    ind-=1
            ans.append(i)
            for i in range(len(temp)):
                ans.append(temp.pop())
        return(list(ans))
s=Solution()
print(s.sorted([3,2,1]))