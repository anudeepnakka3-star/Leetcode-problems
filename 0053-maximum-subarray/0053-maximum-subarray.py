class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp=float('-inf')
        ans=0
        n=len(nums)
        for r in range(n):
            ans+=nums[r]
            if ans>temp:
                temp=ans
            if ans<0:
                ans=0
        return temp
           
            
        