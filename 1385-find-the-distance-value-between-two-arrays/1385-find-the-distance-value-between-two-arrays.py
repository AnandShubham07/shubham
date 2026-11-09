class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        def find_x(a):
            low=a-d
            high=a+d
            left=0
            right=len(arr2)-1
            while(left<=right):
                mid=(left+right)//2
                if low <= arr2[mid] <= high:
                    return 0
                elif arr2[mid]<=low:
                    left=mid+1
                else:
                    right=mid-1
            return 1
        count=0
        for elem in arr1:
            count+=find_x(elem)
        return count

        


        