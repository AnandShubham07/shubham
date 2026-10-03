class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n=len(nums)
        left=0
        right=0
        maxi=0
        i=0
        th=k
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
                    length=right-left
                    if(length > maxi):
                        maxi=length
                    if(nums[left]==0):
                        k+=1
                    left+=1
        length=right-left
        if(length > maxi):
            maxi=length
        return maxi

        