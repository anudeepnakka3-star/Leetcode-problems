class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        max1=nums[n-1]
        max2=nums[n-2]
        return (max1-1)*(max2-1)
