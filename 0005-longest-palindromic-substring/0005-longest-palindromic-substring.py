class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,l,r):
            n=len(s)
            while (l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        start=0
        end=0
        for i in range(len(s)):
            len1=expand(s,i,i)
            len2=expand(s,i,i+1)
            max_len=max(len1,len2)
            if max_len>(end-start):
                start=i-(max_len-1)//2
                end=i+(max_len)//2
        return s[start:end+1]