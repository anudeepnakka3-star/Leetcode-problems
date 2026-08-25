class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        for i in range(1,max(nums)+2):
            if k*i not in num:
                return k*i
                break
        return k
        