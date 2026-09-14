class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n=str(num)
        l=0
        temp=""
        ans=0
        for r in range(len(n)):
            temp+=n[r]
            if len(temp)>k:
                temp=temp[1:]
                l+=1
            if r-l+1==k:
                if int(temp)!=0 and num%int(temp)==0:
                    ans+=1
        return ans

        