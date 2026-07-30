class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        c=0
        for i in range(n):
            if i<8:
                c+=1
            elif i>=8 and i<16:
                c+=2
            elif i>=16 and i<24:
                c+=3
            else:
                c+=4
        return c