class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        prefsum=[0]*n
        prefsum[0]=nums[0]
        for i in range(1,n):
            prefsum[i]=nums[i]+prefsum[i-1]
        return prefsum
        