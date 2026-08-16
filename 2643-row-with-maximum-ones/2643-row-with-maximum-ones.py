class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        c=0
        index=0
        for i in range(rows):
            cnt=0
            for j in range(cols):
                if mat[i][j]==1:
                    cnt+=1
            if cnt>c:
                c=cnt
                index=i
        return [index,c]
        