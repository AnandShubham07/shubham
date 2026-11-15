class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        count=0
        n=len(arr)
        even=0
        odd=0
        for i in range(0,n):           
            if(arr[i]%2==0):
                even+=1
            else:
                even,odd=odd,even
                odd+=1
            count+=odd
        return count%(10**9+7)