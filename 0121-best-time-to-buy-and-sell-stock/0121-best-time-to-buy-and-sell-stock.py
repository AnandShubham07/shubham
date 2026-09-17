class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum=prices[0]
        profit=0
        n=len(prices)
        if n == 1:
            return 0
        for i in range(1,n):
            if prices[i] >= minimum:
                curr_profit = prices[i] - minimum
                if(curr_profit>profit):
                    profit=curr_profit
            else:
                minimum = prices[i]

        return profit
