class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD=10**9 + 7 
        def power(x,y):
            
            res=1
            while y>0:
                if y&1:
                    res=res*x % MOD
                x=x*x % MOD
                y>>=1
            return res
        def decode(num):
            width=num%10
            d=str(num//10)
            x=int(d[0:width])
            y=int(d[width:])
            pow=power(x,y)
            return pow
        ans=0
        n=len(nums)
        for i in range(n):
            ans+=decode(nums[i])
        
        return ans%MOD    