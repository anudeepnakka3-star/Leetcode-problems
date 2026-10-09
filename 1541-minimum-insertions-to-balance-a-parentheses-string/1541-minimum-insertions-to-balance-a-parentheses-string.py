class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        ans=0
        cnt=0
        idx=0
        while idx<n:
            if s[idx]=="(":
                cnt+=1
                idx+=1
            else:
                if cnt>0:
                    cnt-=1
                else:
                    ans+=1
                if idx<n-1 and s[idx+1]==")":
                    idx+=2
                else:
                    ans+=1
                    idx+=1
        ans+=cnt*2
        return ans
            

        
        