class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n=len(nums)
        l=0
        ans=0
        zerocnt=0
        for r in range(n):
            if nums[r]==0:
                zerocnt+=1
            while zerocnt>1:
                if nums[l]==0:
                    zerocnt-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans-1

        