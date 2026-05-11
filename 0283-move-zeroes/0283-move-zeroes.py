class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=-1
        right= 0
        for i in range(0,len(nums)):
            if(nums[i]==0):
                right= right+1
            else:
                right=right+1
                left =left+1
                nums[left]=nums[i]
        for i in range(left+1,len(nums)):
            nums[i]=0
        
                
        