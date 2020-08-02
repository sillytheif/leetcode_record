# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        N = len(intervals)
        begin = 0
        end = N - 1
        while begin <= end:
            mid = (begin+end)>>1
            if newInterval.start>=intervals[mid].start:
                if intervals[mid+1].start>newInterval.start:
                    break
                else:
                    end = mid - 1
            else:
                begin = mid + 1
        while