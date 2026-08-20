class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        count=0
        while(left<=right):
            if nums[left]==val:
                if(nums[right]==val):
                    right=right-1
                else:
                    nums[left],nums[right]=nums[right],nums[left]
                    left=left+1
                    right=right-1
                    count+=1
            else:
                left+=1
                count+=1
        return count

        