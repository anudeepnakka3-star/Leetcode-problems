class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        high=x
        ans=0
        while low<=high:
            mid=(low+high)//2
            midSquare=mid*mid
            if midSquare>x:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans