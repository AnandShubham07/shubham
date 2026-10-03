class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        s=sorted(nums)
        target=k
        left=0
        right=len(s)-1
        count=0
        while(left<right):
            if(s[left]+s[right]==target):
                s.pop(left)
                right-=1
                s.pop(right)
                right-=1
                count+=1

            elif(s[left]+s[right]>target):
                right-=1
            else:
                left+=1
        return count
        
            



        