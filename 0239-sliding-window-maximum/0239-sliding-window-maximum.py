from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        stack=deque()
        n=len(nums)
        for i in range(n):
            if len(stack)!=0 and stack[0]<=i-k:
                stack.popleft()
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            stack.append(i)
            if i>=k-1:
                res.append(nums[stack[0]])
        return res

        