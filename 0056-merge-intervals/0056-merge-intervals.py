class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=len(intervals)        
        j=0
        intervals.sort()
        arr=[intervals[0]]
        for i in range(1,l):
            if(arr[-1][1]>=intervals[i][0]):
                if(arr[-1][1]<intervals[i][1]):
                    arr[-1][1]=intervals[i][1]

            else:
                j+=1
                arr.append([])
                arr[j].append(intervals[i][0])
                arr[j].append(intervals[i][1])
  
        return arr
        