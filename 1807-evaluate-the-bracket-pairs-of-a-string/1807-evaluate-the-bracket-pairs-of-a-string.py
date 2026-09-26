class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dici={}
        for i in range(len(knowledge)):
            dici[knowledge[i][0]]=knowledge[i][1]
        open_brac=-1
        closed_brac=0
        res=""
        for i in range(len(s)):
            if s[i]=="(":
                open_brac=i
                continue
            elif s[i]==")":
                word=s[open_brac+1:i]
                if word in dici:
                    res+=dici[word]
                else:
                    res+="?"
                open_brac=-1
                continue
            elif open_brac==-1:
                res+=s[i]
        return res
