class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n<=3:
            return 0
        
        mini=min(
            nums[n-2]-nums[1],
            nums[n-1]-nums[2],
            nums[n-3]-nums[0]
        )
        return mini

        