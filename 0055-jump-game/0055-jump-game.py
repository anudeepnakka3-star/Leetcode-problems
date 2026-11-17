class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxidx=0
        for i in range(len(nums)):
            if i>maxidx:
                return False
            else:
                maxidx=max(maxidx,i+nums[i])
        return True