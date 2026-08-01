class Solution:
    def numsDivision(self,nums,mid):
        ans=0
        for num in nums:
            ans+=(num+mid-1)//mid
        return ans
                

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            
            if self.numsDivision(nums,mid)>threshold:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans

                
        return res
                



        