class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        right=1
        n=len(nums)
        curr_sum=nums[0] if n else 0
        curr=n+1
        while(left<=right and left!=n):
            if(curr_sum<target):
                if(right<n):
                    curr_sum+=nums[right]
                    right+=1
                else:
                    break

            else:
                length=right-left
                if(length<=curr):
                    curr=length
                curr_sum-=nums[left]
                left+=1

        return 0 if curr==n+1 else curr
            
            
                
        


        