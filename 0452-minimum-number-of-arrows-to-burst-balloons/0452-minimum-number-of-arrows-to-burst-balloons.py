class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        end=float("-inf")
        count=0
        for start,finish in points:
            if start>end:
                count+=1
                end=finish
        return count
        