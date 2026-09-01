class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        n=len(nums)
        for i in range(n):
            xor=xor^nums[i]
        rightmost=xor^(xor&(xor-1))
        b1=0
        b2=0
        for i in range(n):
            if nums[i]&rightmost:
                b1=b1^nums[i]
            else:
                b2=b2^nums[i]
        return [b1,b2]