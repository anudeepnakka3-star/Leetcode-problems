class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        c=0
        while(val in nums):
            nums.remove(val)

        return len(nums)
        return nums




            
            
        