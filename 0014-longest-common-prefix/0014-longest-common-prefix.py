class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base=strs[0]
        res=""
        for i in range(len(base)):
            for s in strs[1:]:
                if i==len(s) or base[i]!=s[i]:
                    return res
                
            res+=base[i]
        return res

        