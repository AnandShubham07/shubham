class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l=len(nums)
        count1=1
        curr1=1
        count2=1
        curr2=1
        #strictly increasing
        for i in range(1,len(nums)):
            if (nums[i]>nums[i-1]):
                curr1+=1
                if (count1<curr1):
                    count1=curr1
            else:               
                    curr1=1
        #strictly decreasing 
        for i in range(1,len(nums)):
            if (nums[i]<nums[i-1]):
                curr2+=1
                if (count2<curr2):
                    count2=curr2
            else:               
                    curr2=1
        return max(count2,count1)   
        