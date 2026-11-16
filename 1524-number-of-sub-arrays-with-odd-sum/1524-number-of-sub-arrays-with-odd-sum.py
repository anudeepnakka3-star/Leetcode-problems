class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        even_count=1
        odd_count=0
        tot=0
        ans=0
        MOD=10**9 +7
        for i in range(n):
            tot+=arr[i]
            if tot%2==1:
                ans=(ans+even_count)%MOD
                odd_count+=1
            elif tot%2==0:
                ans=(ans+odd_count)%MOD
                even_count+=1
        return ans