class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        dici={}
        for i in range(n):
          if nums[i] not in dici:
            dici[nums[i]]=[i]
          else:
            dici[nums[i]].append(i)

        
        ans=0
        for key,val in dici.items():
          if len(val)>=3:
            diff=val[1]-val[0]
            flag=True
            for i in range(2,len(val)):
                if val[i]-val[i-1]!=diff:
                    flag=False
                    break
            if flag:
                ans+=1

                
        return ans
        