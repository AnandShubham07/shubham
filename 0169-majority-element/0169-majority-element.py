class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        n=len(nums)
        for i in range (0,len(nums)):
            if nums[i] in dict:
              dict[nums[i]]=dict[nums[i]]+1
            else:
                dict[nums[i]]=1
        for key in dict:
            if(dict[key]>n/2):
                return key