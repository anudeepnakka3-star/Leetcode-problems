class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n=len(nums)
        max1=nums[0]*nums[1]*nums[2]
        max2=nums[n-1]*nums[n-2]*nums[0]
        return max(max1,max2)
        