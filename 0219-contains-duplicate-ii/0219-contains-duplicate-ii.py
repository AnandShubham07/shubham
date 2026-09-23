class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        l={}
        for i in range(0,len(nums)):
            if(nums[i] not in l ):
                l[nums[i]]=i
            else:
                if (abs(l[nums[i]]-i)<=k):
                    return True
                else:
                    l[nums[i]]=i
        return False





                
        