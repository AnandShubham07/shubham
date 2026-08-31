class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        l=len(intervals)
        j=0
        arr=[intervals[0]]


        for i in range(0,l):
            if(arr[-1][1]>=intervals[i][0]):
                if(arr[-1][1]<intervals[i][1]):
                    arr[-1][1]=intervals[i][1]
                                               
            else:
                arr.append([])
                arr[-1].append(intervals[i][0])
                arr[-1].append(intervals[i][1])
        intervals=arr
        return intervals

            
        