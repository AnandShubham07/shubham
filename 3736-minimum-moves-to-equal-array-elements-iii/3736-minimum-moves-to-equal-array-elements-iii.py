class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        sumn=sum(nums)
        maxi=max(nums)
        return abs(sumn-n*maxi)
        