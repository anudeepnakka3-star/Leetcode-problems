class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        n=len(prices)
        ans=prices
        for i in range(n):
            while stack and prices[stack[-1]]>=prices[i]:
                e=stack.pop()
                ans[e]=prices[e]-prices[i]
            stack.append(i)
        return ans

        