class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=0
        r=0
        n=len(nums)
        pos=[]
        neg=[]
        for i in range(n):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        result=[]
        l=len(pos)
        for p in range(l):
            result.append(pos[p])
            result.append(neg[p])
        return result




            
        