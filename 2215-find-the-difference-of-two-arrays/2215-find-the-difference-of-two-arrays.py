class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        result=[[],[]]
        set1=set(nums1)
        set2=set(nums2)
        for num in set1:
            if(num not in nums2):
                result[0].append(num)
        for num in set2:
            if(num  not in nums1):
                result[1].append(num)
        return result

        