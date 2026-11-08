class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        n=len(s1)
        ans=[]
        i=0
        while i<n:
            if s1[i]==s2[i]:
                i+=1
                continue
            
            start=i
            while i<n and s1[i]!=s2[i]:
                i+=1
            sub1=s1[start:i]
            sub2=s2[start:i]

            ans.append([sub1,sub2])
        return ans

        

        