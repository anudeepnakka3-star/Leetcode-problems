class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        longest_count=0
        
        for num in arr:
            if num-1 not in arr:
                x=num
                count=1
                while x+1 in arr:
                    count+=1
                    x+=1
                longest_count=max(longest_count,count)
        return longest_count
            



                

        return res




        