class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        left_sum=0
        right_sum=sum(nums[1:n])
        for i in range(0,n):
            if(left_sum==right_sum):
                return i
            if(i==n-1):
                return -1

            left_sum=left_sum+nums[i]
            right_sum-=nums[i+1]
    

        