class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        dici={}
        for i in range(len(nums)):
            dici[nums[i]]=dici.get(nums[i],0)+1
        ans=[]
        for _ in range(max(dici.values())):
            for val in dici:
                if dici[val]>0:
                    ans.append(val)
                    dici[val]-=1
                
        return ans
                
        