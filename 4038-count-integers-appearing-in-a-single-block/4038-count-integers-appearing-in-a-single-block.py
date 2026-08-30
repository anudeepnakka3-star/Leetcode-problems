class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        unique_set=set()
        removed_set=set()
        total=0
        for i in range(len(nums)):
            if i==0:
                unique_set.add(nums[i])
                total+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                if nums[i] in unique_set:
                    unique_set.remove(nums[i])
                    total-=1
                    removed_set.add(nums[i])
                elif nums[i] not in unique_set:
                    if nums[i] in removed_set:
                        continue
                    else:
                        unique_set.add(nums[i])
                        total+=1
        return total
            
        