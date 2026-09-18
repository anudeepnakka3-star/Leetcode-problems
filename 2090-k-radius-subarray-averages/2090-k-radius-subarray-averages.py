class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        ans=[-1]*n
        temp=0
        window=(2*k) +1
        idx=k
        l=0
        r=0
        if window>n:
            return ans
        for i in range(k):
            temp+=nums[i]
            r+=1
        for i in range(k,n):
            temp+=nums[i]
            
            if r-l==window:
                temp-=nums[l]
                l+=1
            if r-l+1==window:
                res= temp//window
                ans[idx]=res
                idx+=1
            r+=1   
        return ans



                
