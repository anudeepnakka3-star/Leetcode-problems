class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ele=max(nums)
        ans=0
        for i in range(len(nums)):
            ans+=(max_ele-nums[i])
        return ans
        