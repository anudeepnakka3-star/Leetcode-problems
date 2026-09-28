class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        ans=0
        for ch in s:
            if ch=="(":
                c+=1
            elif ch==")":
                c-=1
            ans=max(ans,c)
        return ans
        