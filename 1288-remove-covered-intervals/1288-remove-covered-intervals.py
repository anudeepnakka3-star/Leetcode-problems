class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        interval=0
        max_end=-1
        for start,end in intervals:
            if end>max_end:
                interval+=1
                max_end=end
        return interval
        