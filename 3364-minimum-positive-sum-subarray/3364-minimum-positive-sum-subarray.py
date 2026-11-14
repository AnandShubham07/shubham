class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        mini=float("inf")
        for i in range(0,n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if (j+1-i>=l and j+1-i<=r):
                    if (s<mini and s>0):
                        mini=s
        return -1 if mini==float("inf") else mini
        