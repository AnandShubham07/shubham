class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs.insert(0,0)
        @cache
        def step(i):
            if (i==n):
                return 0
            ans=float("inf")
            for j in range (i+1,min(i+3,n)+1):
                ans=min(ans,costs[j]+(j-i)**2+step(j)) 
                             
            return ans
        return step(0)