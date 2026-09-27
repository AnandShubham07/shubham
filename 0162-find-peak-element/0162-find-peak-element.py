class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left=0
        right=left+1

        while(left<right):
            if(right>len(nums)-1):
                break
            if(nums[left]<nums[right]):
                left+=1
                right+=1
                if(right>len(nums)-1):
                    break
                if(nums[left]>nums[right]):
                    return left
            else:
                left+=1
                right+=1
        if(nums[0]>nums[left]):
            return 0
        else:
         return left
        