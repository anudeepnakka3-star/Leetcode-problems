class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n=len(nums)
        l=0
        ans=0
        temp=0
        dici={}
        for r in range(n):
            if nums[r] not in dici:
                dici[nums[r]]=1
            else:
                temp+=dici[nums[r]]
                dici[nums[r]]+=1
                
            while temp>=k:
                ans+=n-r
                dici[nums[l]]-=1
                temp-=dici[nums[l]]
                if dici[nums[l]]==0:
                    del dici[nums[l]]
                l+=1
        return ans

            
        