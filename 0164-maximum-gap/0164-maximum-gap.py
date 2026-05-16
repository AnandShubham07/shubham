class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        curr=0
        nums.sort()
        if(len(nums)<2):
            return 0
        else:
            for i in range(1,len(nums)):
                if((nums[i]-nums[i-1])>=curr):
                    curr=(nums[i]-nums[i-1])
        return curr
                        