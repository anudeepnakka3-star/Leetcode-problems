class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr1=[nums[0]]
        arr2=[nums[1]]
        i=2
        while i<len(nums):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
                i+=1
            elif arr1[-1]<arr2[-1]:
                arr2.append(nums[i])
                i+=1
        j=0
        while j<len(arr2):
            arr1.append(arr2[j])
            j+=1
        return arr1



        