class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n=len(nums)
        left=0
        right=0
        maxi=-1
        i=0
        th,k=1,1
        while(th>0 and i<n):
            if(nums[i]==1):
                maxi+=1
            else:
                th-=1
                maxi+=1
            i+=1
        
        while(right<n):
            if(nums[right]==1):
                right+=1
            else:
                if(k!=0):
                    k=k-1
                    right+=1
                else:
                    length=right-left-1
                    if(length > maxi):
                        maxi=length
                    if(nums[left]==0):
                        k+=1
                    left+=1
        length=right-left-1
        if(length > maxi):
            maxi=length
        return maxi

        
        