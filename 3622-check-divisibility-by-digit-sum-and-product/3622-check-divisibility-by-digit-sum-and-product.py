class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        prod=1
        for i in str(n):
            j=int(i)
            sum+=j
            prod*=j
        if n%(sum+prod)==0:
            return True
        return False
            

        