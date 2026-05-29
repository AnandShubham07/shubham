class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            if(sum<0):
                sum=0
            if(sum>=0):
                sum=sum+nums[i]
                if(sum>=curr):
                    curr=sum

        return curr
            
        