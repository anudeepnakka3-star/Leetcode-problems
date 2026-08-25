class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        tot_subsets=1<<n
        result=[]
        for num in range(0,tot_subsets):
            lst=[]
            for i in range(0,n):
                if num&(1<<i)!=0:
                    lst.append(nums[i])
            result.append(lst)
        return result
        
        