class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        def atmost(s,k):
            n=len(s)
            dici={}
            l=0
            ans=-1
            for r in range(n):
                if s[r] not in dici:
                    dici[s[r]]=1
                else:
                    dici[s[r]]+=1
                while dici[s[r]]>k:
                    dici[s[l]]-=1
                    if dici[s[l]]==0:
                        del dici[s[l]]

                    l+=1
                ans=max(ans,r-l+1)
            return ans
        return atmost(s,2)
        