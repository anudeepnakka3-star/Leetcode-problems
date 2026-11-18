class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]
        
        intervals.append(newInterval)
        n=len(intervals)
        intervals.sort()
        for i in range(n):
            if len(res)==0 or intervals[i][0]>res[-1][-1]:
                res.append(intervals[i])
            else:
                res[-1][-1]=max(res[-1][-1],intervals[i][1])
        return res