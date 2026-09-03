class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        left=0
        right=n-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return True 
            elif(nums[mid]==nums[right]):
                    right=right-1
            elif(nums[mid]==nums[left]):
                    left=left+1
            elif(nums[mid]<nums[right]):
                if(target>nums[mid] and target<=nums[right]):
                    left=mid+1
                else:
                    right=mid-1
            else:
                if(target>=nums[left] and target<nums[mid]):
                   right=mid-1
                else:
                    left=mid+1
        return False



