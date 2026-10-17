class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquares(n):
            output=0
            while n:
                digit=n%10
                digit=digit**2
                output+=digit
                n=n//10
            return output
        
        visit=set()
        while n not in visit:
            visit.add(n)
            n=sumofsquares(n)
            if n==1:
                return True
        return False
        
        