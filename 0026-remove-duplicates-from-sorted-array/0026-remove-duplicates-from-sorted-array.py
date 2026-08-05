class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        
        n=len(nums)
        for r in range(1,n):
            if nums[r]!=nums[l]:
                nums[l+1]=nums[r]
                l+=1
            else:
                continue
        return l+1
        