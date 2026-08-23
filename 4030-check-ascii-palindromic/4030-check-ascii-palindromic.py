class Solution:
    def isPalindromic(self, s: str) -> bool:
        s1=[]
        for i in range(len(s)):
            s1.append(ord(s[i]))
        s2=[]
        for i in range(len(s1)):
            s2.append(bin(s1[i])[2:].zfill(8))
        res="".join(s2)
        if str(res[::-1])==str(res):
            return True
        return False
            
        
        