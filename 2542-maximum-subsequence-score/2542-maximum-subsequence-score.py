class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs=sorted(zip(nums2,nums1),reverse=True)
        min_heap=[]
        ans=0
        total=0
        for mini,num in pairs:
            heapq.heappush(min_heap,num)
            total+=num

            if(len(min_heap)>k):
                total-=heapq.heappop(min_heap)
            if(len(min_heap)==k):
                ans=max(ans,total*mini)
        return ans