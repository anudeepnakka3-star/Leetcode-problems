class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        if n==1:
            return n
        if n>1:
            if nums[0]>=nums[1]:
                ans+=1
            if nums[n-1]>=nums[n-2]:
                ans+=1
        for i in range(1,n-1):
            if nums[i]>=(nums[i-1]+nums[i+1])/2:
                ans+=1
        return ans
        