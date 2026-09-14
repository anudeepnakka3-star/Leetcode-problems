class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        n=len(nums)
        l=0
        prod=1
        ans=0
        for r in range(n):
            prod*=nums[r]
            while prod>=k:
                prod/=nums[l]
                l+=1
            
            ans+=r-l+1
        return ans
        
        