class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def printrows(rows):
            res=[1]
            ans=1
            for i in range(1,rows):
                ans=ans*(rows-i)
                ans=ans//i
                res.append(ans)
            return res
        pascal=[]
        for j in range(1,numRows+1):
            pascal.append(printrows(j))
        return pascal

        