class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        l=0
        avg=float('-inf')
        tot=0
        for r in range(n):
            tot+=nums[r]
            if r-l==k:
                tot-=nums[l]
                l+=1
            if r-l+1==k:
                avg=max(avg,tot/k)
        return avg

        