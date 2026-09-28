class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new=nums.copy()
        n=len(nums)
        k=k%n
        nums[:]=new[n-k:]+new[:n-k]
        