class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        n=nums[0]
        for i in range(0,len(nums)):
            if (n==nums[i]):
                count=count+1
            else:
                if(count==0):
                    n=nums[i]
                else:
                    count=count-1
        return n
