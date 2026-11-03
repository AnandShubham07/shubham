class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        sumn=0
        nums.sort()
        n=len(nums)
        if (n==1):
            return 0
        target=nums[n//2]
        for i in range(0,n):
            sumn+=abs(nums[i]-target)
        return sumn