class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        fix_val=min(cost1+cost2,costBoth)*min(need1,need2)
        remain=need1-need2
        if remain>0:
            ans=fix_val+min(cost1,costBoth)*remain
        else:
            ans=fix_val+min(cost2,costBoth)*(-1*remain)
        return ans
