class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def next_per(nums):
            nums=nums.copy()
            n=len(nums)-1
            i=n-1
            j=n
            arr=[]
            
            while(i>=0):
                if(nums[i]<nums[i+1]):
                    length=i+1
                    break
                i=i-1
            if(i<0):
                arr.extend(nums[::-1])
                return arr

            while(j>=i+1):
                if(nums[j]<=nums[i]):
                    j=j-1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    break
            arr.extend(nums[:length])
            arr.extend(nums[:length-1:-1])

            return arr

            
        new=[nums.copy()]
        
        while(1):
            new.append(next_per(new[len(new)-1]))
            if(new[len(new)-1]==nums):
                break
        new.pop()
        return new

                
                    
            
                
                    


        