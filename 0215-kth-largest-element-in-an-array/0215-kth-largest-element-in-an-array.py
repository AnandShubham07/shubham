import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap=[-n for n in nums]
        heapq.heapify(max_heap)
        for i in  range(0,k):
            result=heapq.heappop(max_heap)

        return -result
        