class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        vowels=['a','e','i','o','u',"A","E","I","O","U"]
        l=0
        r=n-1
        res=list(s)
        while l<r:
            if res[l] in vowels and res[r] in vowels:
                res[l],res[r]=res[r],res[l]
                l+=1
                r-=1
            elif res[l] in vowels:
                r-=1
            else:
                l+=1
        return "".join(res)
        