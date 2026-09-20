class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        ans=0
        temp=0
        l=0
        for r in range(n):
            temp+=abs(ord(t[r])-ord(s[r]))
            while temp>maxCost:
                temp-=abs(ord(t[l])-ord(s[l]))
                l+=1
            if temp<=maxCost:
                ans=max(ans,r-l+1)
        return ans
        