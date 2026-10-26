class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def count_set_bits(n):
            count = 0
            while n > 0:
                n &= (n - 1)  
                count += 1
            return count
        s1=count_set_bits(a)
        s2=count_set_bits(b)
        if s1>=s2:
            return s1*s2
        else:
            return s2//s1