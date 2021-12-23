class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        dict=[]
        for i in range(n):
            dict.append((end[i],start[i]))
        dict.sort()
        l=-1
        c=0
        for i in range(n):
            if(dict[i][1]>l):
                c+=1
                l=dict[i][0]
        return(c)
a=Solution()
n=6
start=[1,3,0,5,8,5]
end=[2,4,6,7,9,9]
print(a.maximumMeetings(n,start,end))