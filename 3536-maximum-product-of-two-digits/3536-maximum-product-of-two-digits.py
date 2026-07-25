class Solution:
    def maxProduct(self, n: int) -> int:
        digits=[]
        while n>0:
            digit=n%10
            digits.append(digit)
            n=n//10
        max1=max(digits)
        digits.remove(max1)
        max2=max(digits)
        return max1*max2




        


        