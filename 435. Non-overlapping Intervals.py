class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        val = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < val:
                res += 1
            else:
                val = intervals[i][1]
        return res
