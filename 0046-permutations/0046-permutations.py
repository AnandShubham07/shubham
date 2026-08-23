class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def next_per(nums):
            nums=nums.copy()
            n=len(nums)-1
            length=-1
            # if(n==1):
            #     nums.sort(reverse=True)
            #     return nums
            for i in range(n-1,-1,-1):
                if(nums[i]<nums[i+1]):              
                    curr=nums[i+1]
                    index=i+1
                    for j in range(n,i,-1):
                        if(nums[j]>nums[i] ):#and nums[j]<curr
                            curr=nums[j]
                            index=j
                            break
                                
                    nums[i],nums[index]=nums[index],nums[i]        
                    length=i
                    break

            if length == -1:
                nums[:] = nums[::-1]
                return nums
            else:
                nums[length + 1:] = nums[length + 1:][::-1]
                return nums
        

            
        new=[nums.copy()]
        
        while(1):
            new.append(next_per(new[len(new)-1]))
            if(new[len(new)-1]==nums):
                break
        new.pop()
        return new

                
                    
            
                
                    


        