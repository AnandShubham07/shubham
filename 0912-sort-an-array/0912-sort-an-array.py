class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
      
        def merge_sorted_array(arr1, arr2):
            i, j = 0, 0
            result = []

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1

        
            while i < len(arr1):
                result.append(arr1[i])
                i += 1

            while j < len(arr2):
                result.append(arr2[j])
                j += 1
            
            return result

       
        def merge_sort(nums):
            if (len(nums)<=1):
                return nums
            mid = len(nums)//2
            leftArr=nums[:mid]
            rightArr=nums[mid:]
            left=merge_sort(leftArr)
            right=merge_sort(rightArr)
            return merge_sorted_array(left,right)
        
        return merge_sort(nums)
        