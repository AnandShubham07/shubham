class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        
        first=nums[0]
        second=max(nums[1],nums[0])
        for i in range(2,len(nums)):              
               new=max(second,first+nums[i])
               first=second
               second=new               
        return second


        

        

        