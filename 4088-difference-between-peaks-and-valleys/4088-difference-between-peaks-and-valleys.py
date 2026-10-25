class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        n=len(nums)
        sum1=0
        sum2=0
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                sum1+=nums[i]
            if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                sum2+=nums[i]
        return sum1-sum2