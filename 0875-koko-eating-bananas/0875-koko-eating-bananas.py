class Solution:
    def totalhours(self,piles,mid):
        ans=0
        for pile in piles:
                ans+=(pile+mid-1)//mid
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        l=1
        r=max(piles)
        
        while l<=r:
            mid=(l+r)//2
           
            if self.totalhours(piles,mid)>h:
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans
        