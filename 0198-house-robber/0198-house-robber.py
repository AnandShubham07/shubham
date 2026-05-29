class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*(n)
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])           
       
        for i in range(2,len(nums)):
            if(dp[i-1]>dp[i-2]+nums[i]):
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-2]+nums[i]
        return dp[n-1]

        

        