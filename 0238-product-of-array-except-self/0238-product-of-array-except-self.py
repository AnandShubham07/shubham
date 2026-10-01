class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        suffix=1
        dp=[1 for num in nums]
        for i in range(1,n):
            dp[i]=nums[i-1]*dp[i-1]
        for i in range(n-2,-1,-1):
            suffix=suffix*nums[i+1]
            dp[i]=dp[i]*suffix
        return dp



        