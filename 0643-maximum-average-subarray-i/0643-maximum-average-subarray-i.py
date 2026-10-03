class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        if(n==1):
            return nums[0]/1
        curr_sum=sum(nums[0:k])
        curr_avg=(curr_sum)/k
        left=0
        right=left+k        
        while(left<n and right<n):
            curr_sum=curr_sum+nums[right]-nums[left]
            r=curr_sum/k
            if((r)>(curr_avg)):
                curr_avg=r
            left+=1
            right+=1
        return curr_avg

        