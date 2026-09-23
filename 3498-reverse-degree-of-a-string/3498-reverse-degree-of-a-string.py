class Solution:
    def reverseDegree(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            ans+=(ord('z')-ord(s[i])+1)*(i+1)
        return ans

        