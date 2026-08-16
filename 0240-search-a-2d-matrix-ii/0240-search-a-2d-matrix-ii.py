class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        l=0
        r=cols-1
        while (l<rows and r>=0):
            if matrix[l][r]==target:
                return True
            elif matrix[l][r]>target:
                r-=1
            else:
                l+=1
        return False

        