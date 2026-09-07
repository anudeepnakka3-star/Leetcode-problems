class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        stack=[]
        if n==k:
            return "0"
        
        for i in range(n):
            while stack and stack[-1]>num[i] and k>0:
                stack.pop()
                k-=1
            
            stack.append(num[i])
        while stack and (k>0):
            stack.pop()
            k-=1
        if len(stack)==0:
            return '0'
        res=""
        while stack:
            res+=stack[-1]
            stack.pop()
        res = res.rstrip('0')
        res=res[::-1]
        if not res:
            return '0'

        return res
        
        