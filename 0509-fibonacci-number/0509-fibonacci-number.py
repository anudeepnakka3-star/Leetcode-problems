class Solution:
    def func(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.func(n-1)+self.func(n-2)
    def fib(self, n: int) -> int:
        return self.func(n)

        