class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tot=sum(nums)
        n=len(nums)
        k=tot-x
        if k<0:
            return -1
        best=-1
        curr=0
        l=0
        for r in range(n):
            curr+=nums[r]
            while curr>k:
                curr-=nums[l]
                l+=1
            if curr==k:
                best=max(best,r-l+1)
        if best<0:
            return -1
        else:
            return n-best

        