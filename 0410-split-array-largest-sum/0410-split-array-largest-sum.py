class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def suml(nums,k,mid):
            ele=1
            sumele=0
            for i in range(len(nums)):
                if sumele+nums[i]>mid:
                    ele+=1
                    sumele=nums[i]
                else:
                    sumele+=nums[i]
            return ele
        
        l=max(nums)
        r=sum(nums)
        while l<=r:
            mid=(l+r)//2
            if suml(nums,k,mid)>k:
                l=mid+1
            elif suml(nums,k,mid)<=k:
                ans=mid
                r=mid-1
               
        return ans
        