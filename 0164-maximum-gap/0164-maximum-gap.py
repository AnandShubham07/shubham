class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        max_val=max(nums)
        min_val=min(nums)
        if(min_val==max_val):
            return 0

        bucket_size=max(1,(max_val-min_val)//n-1)
        bucket_count=((max_val-min_val)//bucket_size)+1

        bucket=[]
        for i in range(bucket_count):
            bucket.append([None,None])
        for i in range (len(nums)):
            bucket_index=((nums[i]-min_val)//bucket_size)
            

            if bucket[bucket_index][0] is None:
                bucket[bucket_index][0]=nums[i]
                bucket[bucket_index][1]=nums[i]
            else:
                bucket[bucket_index][0]=min(bucket[bucket_index][0],nums[i])
                bucket[bucket_index][1]=max(bucket[bucket_index][1],nums[i])
        max_gap=0
        prev_max=min_val
        for i in range(bucket_count):
            if(bucket[i][0] is None):
                continue
            max_gap=max(max_gap,bucket[i][0]-prev_max)
            prev_max=bucket[i][1]
    
        return max_gap




