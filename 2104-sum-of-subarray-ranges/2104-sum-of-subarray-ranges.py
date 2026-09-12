class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            minele=nums[i]
            maxele=nums[i]
            for j in range(i,n):
                minele=min(nums[j],minele)
                maxele=max(nums[j],maxele)
                ans+=maxele-minele
        return ans
        