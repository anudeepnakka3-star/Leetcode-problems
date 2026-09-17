class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dici={}
        l=0
        r=0
        ans=0
        curr_sum=0
        for r in range(n):
            curr_sum+=nums[r]
            dici[nums[r]] = dici.get(nums[r], 0) + 1 
            if r-l+1>k:
                curr_sum-=nums[l]
                dici[nums[l]]-=1
                if dici[nums[l]]==0:
                    del dici[nums[l]]
                l+=1
            if r-l+1==k and (len(dici)==k):
                ans=max(ans,curr_sum)       
        return ans
        