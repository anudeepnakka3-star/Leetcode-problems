class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n=len(nums)
        for i in range(n):
            max_ele=max(nums[0:i+1])
            min_ele=min(nums[i:n])
            if max_ele-min_ele<=k:
                return i
        return -1

        