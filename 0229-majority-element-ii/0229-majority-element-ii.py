class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[]
        dict={}
        for num in nums:
            dict[num]=0 
        for num in nums:
            dict[num]=dict[num]+1
        for key,value in dict.items():
            if value>n//3:
                result.append(key)
        return result
        