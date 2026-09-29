from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=deque()
        result=[]
        for ch in s:
            if ch=="(":
                stack.append(len(result))
            elif ch==")":
                start=stack.pop()
                result[start:]=result[start:][::-1]
            else:
                result.append(ch)
        return "".join(result)