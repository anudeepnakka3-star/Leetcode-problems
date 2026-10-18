class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n-1):
            if nums[i]^ nums[i+1]==0:
                ans+=1
        return ans