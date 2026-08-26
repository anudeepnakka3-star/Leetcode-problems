class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        l=0
        res=""
        temp=0
        ans=float('inf')
        for r in range(n):
            if s[r]=='1':
                temp+=1
            while temp>k:
                if s[l]=='1':
                     temp-=1
                l+=1
            if temp==k:
                while s[l]=='0':
                    l+=1
                cur=s[l:r+1]
                if len(cur)<ans:
                    res=cur
                    ans=len(cur)
                elif (len(cur)==ans and cur<res):
                    res=cur

                
        return res