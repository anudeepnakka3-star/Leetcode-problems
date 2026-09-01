class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX=2**31-1
        INT_MIN=-(2**31)
        if dividend==divisor:
            return 1
        sign=True
        if (dividend>=0 and divisor<0) or (dividend<0 and divisor>0): 
            sign=False
        
        n,d=abs(dividend),abs(divisor)
        ans=0
        while (n>=d):
            cnt=0
            while (n>=(d<<(cnt+1))):
                cnt+=1
            ans+=1<<cnt
            n=n-(d<<cnt)
        if not sign:
            ans=-ans
        if ans>INT_MAX:
            return INT_MAX
        if ans<INT_MIN:
            return INT_MIN
        return ans
        