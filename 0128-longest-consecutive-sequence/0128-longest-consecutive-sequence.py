class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n=len(nums)
        longest=0
        if(n==0):
            return 0        
        s=set(nums)
        for key in s:
            length=1
            if(key-1 not in s):
                current=key
                while(current+1 in s):
                    current+=1
                    length+=1
            if(length>=longest):
                longest=length
        return longest
            




        