class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        max_ele=max(nums)
        l=0
        ans=0
        max_cnt=0
        for r in range(n):
            if nums[r]==max_ele:
                max_cnt+=1
            while max_cnt>=k:
                ans+=n-r
                if nums[l]==max_ele:
                    max_cnt-=1
                l+=1
                
        return ans



        