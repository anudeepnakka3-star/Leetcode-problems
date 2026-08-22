class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits=[]
        temp=n
        while temp!=0:
            digit=temp%10
            temp=temp//10
            digits.append(digit)
        prod=1
        tot=0
        for i in digits:
            prod*=i
            tot+=i
        if n%(prod+tot)==0:
            return True
        else:
            return False
            

        