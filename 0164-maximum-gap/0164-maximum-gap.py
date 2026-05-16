class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        curr=0
        nums.sort()
        if(len(nums)==1):
            return 0
        else:
            for i in range(len(nums)):
                if((nums[i]-nums[i-1])>=curr):
                    curr=(nums[i]-nums[i-1])
        return curr
                        