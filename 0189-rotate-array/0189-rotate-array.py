class Solution:
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1        
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        r=k%n
        self.reverse(nums,n-r,n-1)
        self.reverse(nums,0,n-r-1)
        self.reverse(nums,0,n-1)
        
        
        

        
            
            


        