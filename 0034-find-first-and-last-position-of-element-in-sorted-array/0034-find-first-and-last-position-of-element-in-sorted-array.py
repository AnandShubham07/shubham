class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target,is_search):
            low=0
            high=len(nums)-1
            c=-1

            while(low<=high):
                mid=(low+high)//2
            
                    
                if(nums[mid]>target):               
                    high=mid-1
                elif(nums[mid]<target): 
                    low=mid+1  
                else:
                    c=mid
                    if is_search:
                        high=mid-1
                    else:
                        low=mid+1
            return c
        low=binary_search(nums,target,True)
        high=binary_search(nums,target,False)


        return [low,high]

                