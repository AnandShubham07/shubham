class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
    
        for i in range(1,len(nums)-1):
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                return i
        return 0 if nums[0]>nums[len(nums)-1] else  len(nums)-1

        