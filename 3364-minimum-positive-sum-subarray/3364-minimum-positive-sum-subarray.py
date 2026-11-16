class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        subarrays=[]
        for i in range(n):
            for length in range(l, r + 1):
                if i + length <= n:
                    subarrays.append(nums[i : i + length])
        ans=float('inf')
        for i in subarrays:
            if sum(i)>0:
                ans=min(ans,sum(i))
        if ans==float('inf'):
            return -1
        return ans
        
