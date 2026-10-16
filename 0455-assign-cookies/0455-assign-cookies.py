class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        m=len(g)
        n=len(s)
        i=0
        j=0
        
        while i<n and j<m:
            if s[i]>=g[j]:
                j+=1
            i+=1
        return j
        