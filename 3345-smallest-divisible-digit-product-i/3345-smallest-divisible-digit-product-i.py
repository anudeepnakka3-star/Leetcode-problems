class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(num):
            prod=1
            
            while num>0:
                temp=num%10
                prod*=temp
                num=num//10
            return prod
        while digitProduct(n)%t!=0:
            n+=1
        return n
        