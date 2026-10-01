class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max=nums[0]
        curr_min=nums[0]
        result=nums[0]
        for num in nums[1:]:
            oldmax=curr_max
            oldmin=curr_min

            curr_max=max(num,oldmax*num,oldmin*num)
            curr_min=min(num,oldmax*num,oldmin*num)

            result=max(result,curr_max)
        return result
