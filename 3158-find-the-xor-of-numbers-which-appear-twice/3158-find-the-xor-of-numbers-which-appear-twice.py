class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hashmp={}
        for i in range(len(nums)):
            if nums[i] not in hashmp:
                hashmp[nums[i]]=1
            else:
                hashmp[nums[i]]+=1
        ans=0
        for i in hashmp:
            if hashmp[i]==2:
                ans=ans^i
        return ans

        