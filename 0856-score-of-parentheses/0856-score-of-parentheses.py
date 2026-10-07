class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        ans=0
        for ch in s:
            if ch=="(":
                stack.append(0)
            else:
                e=stack.pop()
                stack[-1]+=max(2*e,1)
        return stack.pop()
        