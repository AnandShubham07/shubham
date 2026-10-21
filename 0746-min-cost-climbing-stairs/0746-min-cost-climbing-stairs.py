class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo={}
        def step(i):
            if (i in memo):
                return memo[i]
            if (i>=len(cost)):
                return 0
            else:
                memo[i]=(min(step(i+1),step(i+2))+cost[i])
                return memo[i]
        return(min(step(0),step(1)))