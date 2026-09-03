class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        i=2
        if(n<=2):
            return n
        while(i<n):
            if(nums[i]=="-"):
                break
            if(nums[i]==nums[i-1] and nums[i-1]==nums[i-2]):
                nums.remove(nums[i])
                nums.append("-")
                c+=1
                i-=1
            i+=1
                
        return n-c
            


        