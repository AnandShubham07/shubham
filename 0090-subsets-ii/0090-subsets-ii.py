class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        left=0
        right=1
        new=[]
        if(n==0):
            return new
        nums.sort()
        start=0
        def subset(start,current):
            new.append(current[:])
            for i in range(start,n):
                if(i>start and nums[i]==nums[i-1]):
                    continue
                current.append(nums[i])
                subset(i+1,current)

                current.pop()

    
        subset(0,[])
        return new
        


            

        