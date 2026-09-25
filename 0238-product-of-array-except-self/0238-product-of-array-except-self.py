class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod=1
        n=len(nums)
        prefprod=[1]*n
        
        for i in range(1,n):
            prefprod[i]=prefprod[i-1]*nums[i-1]
        suffprod=[1]*n
        for i in range(n-2,-1,-1):
            suffprod[i]=suffprod[i+1]*nums[i+1]
        for i in range(n):
            nums[i]=prefprod[i]*suffprod[i]
        return nums
            
        