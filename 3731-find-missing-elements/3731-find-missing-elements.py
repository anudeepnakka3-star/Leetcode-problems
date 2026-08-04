class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minele=min(nums)
        maxele=max(nums)
        res=[]
        for i in range(minele,maxele+1):
            if i not in nums:
                res.append(i)

                
        return res
        