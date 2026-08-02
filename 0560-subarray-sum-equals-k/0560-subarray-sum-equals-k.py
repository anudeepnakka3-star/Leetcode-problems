class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dici={}
        dici[0]=1
        prefsum=0
        cnt=0
        for i in range(n):
            prefsum+=nums[i]
            remove=prefsum-k
            if remove in dici:
                cnt+=dici[remove]
            dici[prefsum] = dici.get(prefsum, 0) + 1
        return cnt
          
        