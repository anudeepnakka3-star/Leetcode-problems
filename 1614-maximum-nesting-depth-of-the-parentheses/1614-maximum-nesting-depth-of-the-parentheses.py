class Solution:
    def maxDepth(self, s: str) -> int:
        n=len(s)
        c=0
        ans=0
        for i in range(n):
            if s[i]=="(":
                c+=1
            elif s[i]==")":
                c-=1
            ans=max(c,ans)
        return ans
        