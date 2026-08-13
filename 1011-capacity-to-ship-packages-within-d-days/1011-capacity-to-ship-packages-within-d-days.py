class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacity(weights,mid):
            day=1
            load=0
            for i in range(len(weights)):
                if load+weights[i]>mid:
                    day+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            return day
        
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=(l+r)//2
            if capacity(weights,mid)>days:
                
                l=mid+1
            else:
                
                r=mid-1
        return l
        