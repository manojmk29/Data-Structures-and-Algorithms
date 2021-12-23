nums=[1,2,3]
ans=[]
first=[]
n=len(nums)
def helper(pos,arr,ans):
    if(pos==n):
        ans+=[arr]
        return
    arr+=[nums[pos]]
    helper(pos+1,arr,ans)
    arr.pop()
    helper(pos+1,arr,ans)
helper(0,first,ans)
print(ans)