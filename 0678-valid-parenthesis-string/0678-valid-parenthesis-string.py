class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        minopen=0
        maxopen=0
        for i in range(n):
            if s[i]=="(":
                minopen+=1
                maxopen+=1
            elif s[i]==")":
                minopen-=1
                maxopen-=1
            else:
                minopen-=1
                maxopen+=1
            if maxopen<0:
                return False
            minopen=max(0,minopen)
        return minopen==0
        