class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        top=0
        bottom=r-1
        left=0
        right=c-1
        res=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    res.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for a in range(bottom,top-1,-1):
                    res.append(matrix[a][left])
                left+=1
        
        return res



        
        