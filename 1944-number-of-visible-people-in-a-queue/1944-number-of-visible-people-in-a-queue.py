class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n=len(heights)
        stack=[]
        ans=[0]*n
        
        for i in range(n):
            while stack and heights[stack[-1]]<=heights[i]:
                e=stack.pop()
                ans[e]+=1
            if len(stack)!=0:
                ans[stack[-1]]+=1
            stack.append(i)
        return ans
            
        