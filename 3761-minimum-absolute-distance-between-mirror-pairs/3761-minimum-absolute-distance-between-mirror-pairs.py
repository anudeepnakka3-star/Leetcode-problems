class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dici={}
        ans=float("inf")
        for i in range(len(nums)):
            num=nums[i]
            if num in dici:
                ans=min(ans,i-dici[num])
            dici[int(str(num)[::-1])]=i 
        if ans==float('inf'):
            return -1
        else:
            return ans