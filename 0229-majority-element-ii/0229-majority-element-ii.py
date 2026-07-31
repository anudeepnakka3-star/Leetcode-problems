class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dici={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in dici:
                dici[nums[i]]=1
            else:
                dici[nums[i]]+=1
        res=[]
        for num in dici:
            if dici[num]>n//3:
                res.append(num)
        return res

        