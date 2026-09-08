class Solution:
    def countCommas(self, n: int) -> int:
        '''
        if n<1000:
            return 0
        else:
            ans=0
            for i in range(1000,n+1):
                ans+=1
            return ans
        '''
        return max(n-999,0)
                

        