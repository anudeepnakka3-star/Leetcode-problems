class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        dici={}
        i=0
        for i in range(len(nums)):
            if nums[i] not in dici:
                dici[nums[i]]=1
            else:
                dici[nums[i]]+=1
        sorted_dici = dict(sorted(dici.items(), key=lambda item: item[1], reverse=True))
        res=[]
        for i in sorted_dici:
            res.append(i)
        return res[:k]


        