class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tot_len=len(nums1)+len(nums2)
        odd=1
        if(tot_len%2==0):
            odd=0
        arr=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<nums2[j]):
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            arr.append(nums1[i])
            i+=1
        while( j<len(nums2)):
            arr.append(nums2[j])
            j+=1
        if(odd==1):
            return(arr[tot_len//2])
        else:
            tt=(tot_len)//2
            tot=arr[tt]+arr[tt-1]
            return(float(tot)/2)