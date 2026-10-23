class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        new=sorted(intervals,key=lambda x:x[1])
        count=0
        end=float("-inf")
        for i in range(0, len(new)):
            if new[i][0]<end:
                count+=1
            else:
                end=new[i][1]
        return count


        