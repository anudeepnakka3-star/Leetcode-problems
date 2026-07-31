class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici={}
        for i in s:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        dici1={}
        for i in t:
            if i in dici1:
                dici1[i]+=1
            else:
                dici1[i]=1
        if dici==dici1:
            return True
        else:
            return False

        