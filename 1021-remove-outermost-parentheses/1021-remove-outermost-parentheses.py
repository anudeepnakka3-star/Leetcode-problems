class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n=len(s)
        s1=""
        c=0
        for i in range(n):
            
            if s[i]=="(":
                
                if c>0:
                    s1+="("
                c+=1
            if s[i]==")":
                c-=1
                if c>0:
                    s1+=")"
                
        return s1
            
        