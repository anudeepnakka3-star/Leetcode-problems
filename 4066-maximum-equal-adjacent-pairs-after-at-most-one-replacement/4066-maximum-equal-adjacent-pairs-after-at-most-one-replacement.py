from collections import defaultdict
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        dici=defaultdict(int)
        for i in range(1,n):
            a=nums[i-1]
            b=nums[i]
            if a==b:
                ans+=1
            else:
                dici[(a,b)]+=1
                dici[(b,a)]+=1
        res=0
        for i in dici.values():
            res=max(res,i)
        return ans+res
                
        
        