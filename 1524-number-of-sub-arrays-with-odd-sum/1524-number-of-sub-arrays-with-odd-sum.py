class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        count=0
        n=len(arr)
        prefix=0
        even=1
        odd=0
        for i in range(0,n):           
            prefix+=arr[i]
            if(prefix%2==0):
                count+=odd
                even+=1
            else:
                count+=even
                odd+=1
        return count%(10**9+7)
            