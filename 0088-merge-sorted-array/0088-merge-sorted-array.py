class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left=n-1
        right=m-1
        for i in range(m+n-1,-1,-1):
            if(right<0):
                nums1[i]=nums2[left]
                left-=1
            elif(left<0 ):
                break
            elif(nums1[right]<nums2[left]):
                nums1[i]=nums2[left]
                left-=1
            else:
                nums1[i],nums1[right]=nums1[right],nums1[i]
                right-=1
                
        