class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nextsmaller=[n]*n
        previoussmaller=[-1]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                e=stack.pop()

                nextsmaller[e]=i
            if len(stack)!=0:
                previoussmaller[i]=stack[-1]
            stack.append(i)
        area=0
        for i in range(n):
            height=heights[i]
            width=nextsmaller[i]-previoussmaller[i]-1
            area=max(area, height*width)
        return area