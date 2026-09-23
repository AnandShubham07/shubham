class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l=set()
        for i in range(0,len(nums)):
            if(nums[i] in l):
                return True 
            l.add(nums[i])
            if(i>=k):
                l.remove(nums[i-k])
        return False





                
        