class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        profit=0
        minimum=prices[0]
        for i in range(0,n):
            if(prices[i]>=minimum):
                curr=prices[i]-minimum               
                profit+=curr
                minimum=prices[i]
                
            else:
                minimum=prices[i]
        return profit

        