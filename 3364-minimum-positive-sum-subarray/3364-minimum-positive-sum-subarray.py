class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        mini=float("inf")
        for i in range(0,n):
            for j in range(i,n):
                if (j+1-i>=l and j+1-i<=r):
                    s=sum(nums[i:j+1])
                    if (s<mini and s>0):
                        mini=s
        return -1 if mini==float("inf") else mini
        