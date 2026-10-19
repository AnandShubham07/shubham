class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        total=0
        h1=costs[:candidates]
        h2=costs[max(candidates,len(costs)-candidates):]
        heapq.heapify(h1)
        heapq.heapify(h2)
        left=candidates
        right=len(costs)-candidates-1
        while(k>0):
            
            if(left>right):
                h1=h1+h2
                heapq.heapify(h1)
                break
            else:                
                if(h1[0]<=h2[0]):
                    total+=heapq.heappop(h1)
                    k-=1
                    heapq.heappush(h1,costs[left])
                    left+=1
                else:
                    total+=heapq.heappop(h2)
                    k-=1
                    heapq.heappush(h2,costs[right])
                    right-=1
        if(k==0):
            return total
        else:
            while(k>0):
                total+=heapq.heappop(h1)
                k-=1
            return total
        