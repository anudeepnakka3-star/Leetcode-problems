class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        i=0
        while n!=0:
            nums.append(start+(2*i))
            i+=1
            n-=1   
        ans=0
        for i in nums:
            ans=ans^i
        return ans     