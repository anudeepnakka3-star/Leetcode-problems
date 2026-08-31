class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones=0
        twos=0
        for i in range(len(nums)):
            ones=(nums[i]^ones)&(~twos)
            twos=(nums[i]^twos)&(~ones)
        return ones
           