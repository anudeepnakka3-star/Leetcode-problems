class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        arr=set(nums)
        n=len(nums)
        ans=0
        dici={}
        l=0
        for r in range(n):
            if nums[r] not in dici:
                dici[nums[r]]=1
            else:
                dici[nums[r]]+=1
            while len(dici)>=len(arr):
                ans+=n-r
                dici[nums[l]]-=1
                if dici[nums[l]]==0:
                    del dici[nums[l]]
                l+=1
            
        return ans

            
        