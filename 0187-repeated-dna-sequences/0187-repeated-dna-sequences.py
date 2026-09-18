class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        k=10
        dici={}
        n=len(s)
        l=0
        res=""
        for r in range(n):
            res+=s[r]
            if r-l==k:
                res=res[1:]
                l+=1
            if r-l+1==k:
                if res not in dici:
                    dici[res]=1
                else:
                    dici[res]+=1
        ans=[]
        for key,val in dici.items():
            if val>1:
                ans.append(key)
        return ans
