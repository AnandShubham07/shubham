class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def check_jump(index):
            i=index-1
            dis=index-i
            l=dis
            while(i>=0):
                if((nums[i]>=dis and nums[i]<=l )or nums[i]==0):
                    i=i-1
                    l+=1               
                else:
                        return True
            return False
        n=len(nums)
        if(nums[0]==0):
            if(n==1):
                return True
            else:
                return False
        if 0 in nums[0:n-1]:
            for i  in range(n-2,-1,-1):
                if (nums[i]==0):
                    index=i
                    if(check_jump(index)):
                        continue
                    else:
                        return False
            return True
        else:
            return True

                    
                    
        