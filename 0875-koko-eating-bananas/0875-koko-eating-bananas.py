class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        right=max(piles)
        left=1
        while(left<=right):
            mid=(left+right)//2
            total=0
            for i in range(len(piles)):
                num=(piles[i]+mid-1)//mid
                total+=num
            if(total<=h):
                right=mid-1
            else:
                left=mid+1
        return left
        