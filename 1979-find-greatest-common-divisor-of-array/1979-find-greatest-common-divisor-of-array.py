class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        gc=float('inf')
        while b:
            a,b=b,a%b
            gc=min(gc,a)
        return gc
            
        