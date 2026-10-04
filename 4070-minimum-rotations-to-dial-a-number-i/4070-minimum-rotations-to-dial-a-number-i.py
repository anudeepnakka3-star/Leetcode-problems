class Solution:
    def minRotations(self, s: str) -> int:
        n=len(s)
        
        ans=0
        for r in range(0,n):
            if r==0:
                a=0
            else:
                a=int(s[r-1])
            b=int(s[r])
            ans+=min(abs(a-b),10-abs(a-b))
           
        return ans

        
        