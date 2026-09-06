class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return -1
        prefmax=[0]*n
        prefmax[0]=nums[0]
        for i in range(1,n):
            prefmax[i]=max(prefmax[i-1],nums[i])
        suffmin=[0]*n
        suffmin[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffmin[i]=min(suffmin[i+1],nums[i])
        for i in range(n):
            if prefmax[i]-suffmin[i]<=k:
                return i
        return -1
        