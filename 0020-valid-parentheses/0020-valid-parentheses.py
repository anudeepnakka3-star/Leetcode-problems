class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ans=True
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                e=stack.pop()
                if (
                    (i==")" and e=="(") or
                    (i=="]" and e=="[") or 
                    (i=="}" and e=="{")
                ):
                    continue
                else:
                    return False
        return len(stack)==0
                
        
