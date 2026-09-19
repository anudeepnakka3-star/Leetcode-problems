class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n=len(nums)
        l=0
        r=0
        count=0
        temp=0
        while r<n:
            temp+=nums[r]
            while l<=r and  (temp)*(r-l+1)>=k:
                temp-=nums[l]
                l+=1
            count+=(r-l+1)
            r+=1
        return count
           
        