class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        if n==0:
            return 0
        s1=s.replace('0',"")
        s2=int(s1)
        s3=int(s1)
        tot=0
        while s2>0:
            digit=s2%10
            tot+=digit
            s2=s2//10
        return (tot*s3)

        