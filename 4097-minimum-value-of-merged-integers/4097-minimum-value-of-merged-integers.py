class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        n=len(nums)
        ans=float('inf')
        for i in range(0,n,2):
            num=str(nums[i])+str(nums[i+1])
            if int(num)<ans:
                ans=int(num)
        return ans