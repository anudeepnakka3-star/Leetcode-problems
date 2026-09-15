class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l=0
        dici={}
        max_freq=0
        ans=0
        for r in range(n):
            if s[r] not in dici:
                dici[s[r]]=1
            else:
                dici[s[r]]+=1
            max_freq=max(max_freq,dici[s[r]])
            while (r-l+1)-max_freq>k:
                dici[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
            
        

        