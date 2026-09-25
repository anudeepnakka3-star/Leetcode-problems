class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        dici={}
        for i in range(n):
            if nums[i] not in dici:
                dici[nums[i]]=1
            else:
                dici[nums[i]]+=1
                return True
        return False
        

        