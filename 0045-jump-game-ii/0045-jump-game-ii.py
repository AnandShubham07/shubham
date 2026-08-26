class Solution:
   
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        ptr=0
        jump=0

        while(ptr<n-1):
            curr=nums[ptr]+ptr
            if(curr<n-1):
                maximum=0
                for i in range(ptr+1,curr+1):
                    if(i+nums[i]>maximum):
                        maximum=i+nums[i]
                        new_ptr=i
                ptr=new_ptr
                jump+=1
            else:
                return jump+1
                
        return jump



       