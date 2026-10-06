class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for ch in s:
            if ch=="(":
                stack.append("(")
                ans+=1
            if ch==")":
                if stack:
                    stack.pop()
                    ans-=1
                elif len(stack)==0:
                    ans+=1

        return ans
        