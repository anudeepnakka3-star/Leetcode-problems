class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        res=[]
        if n==1:
            res.append(intervals[0])
        else:
            for i in range(n):
                if len(res)==0 or intervals[i][0]>res[-1][-1]:
                    res.append(intervals[i])
                else:
                    res[-1][-1]=max(res[-1][-1],intervals[i][1])
        return res


        