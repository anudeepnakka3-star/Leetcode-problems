class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        leftprod=1
        rightprod=1
        ans=nums[0]
        for i in range(n):
            if leftprod==0:
                leftprod=1
            if rightprod==0:
                rightprod=1
            leftprod*=nums[i]
            rightprod*=nums[n-1-i]
            ans=max(ans,max(leftprod,rightprod))
        return ans
        
        