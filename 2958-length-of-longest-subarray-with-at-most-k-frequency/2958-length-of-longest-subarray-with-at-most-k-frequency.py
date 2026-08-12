class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        def atmostk(nums,k):
            n=len(nums)
            l=0
            dici={}
            ans=0
            for r in range(n):
                if nums[r] not in dici:
                    dici[nums[r]]=1
                else:
                    dici[nums[r]]+=1
                while dici[nums[r]]>k:
                    dici[nums[l]]-=1
                    
                    l+=1
                ans=max(ans,r-l+1)
            return ans
        
        return atmostk(nums,k)


        