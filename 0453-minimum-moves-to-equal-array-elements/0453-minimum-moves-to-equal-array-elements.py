class Solution:
    def minMoves(self, nums: list[int]) -> int:
        sumn=sum(nums)
        mini=min(nums)
        n=len(nums)
        return sumn-mini*n
        