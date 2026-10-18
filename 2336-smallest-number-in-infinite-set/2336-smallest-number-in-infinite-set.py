import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.h=[1]
        heapq.heapify(self.h)
    def popSmallest(self) -> int:
            if (self.h):
                r=heapq.heappop(self.h)
                if not self.h:
                    heapq.heappush(self.h,r+1)
                return r

    def addBack(self, num: int) -> None:
        if num  not in self.h and num < max(self.h):
            heapq.heappush(self.h,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)