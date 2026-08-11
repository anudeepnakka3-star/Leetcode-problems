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
        for j in range(numRows):
            pascal.append(printrows(numRows-j))
        return pascal[::-1]

        