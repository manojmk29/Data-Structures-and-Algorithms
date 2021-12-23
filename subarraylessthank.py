def numSubarrayProductLessThanK( nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
nums=[10,11,12,13]
k=0
print(numSubarrayProductLessThanK(nums,k))