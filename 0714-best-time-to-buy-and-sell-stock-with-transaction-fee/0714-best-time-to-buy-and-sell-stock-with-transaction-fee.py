class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        #buy==1 means available to buy new stock
        #buy=0 means not available to buy 
        memo={}
        def sp(i,buy):
            if ((i,buy) in memo):
                return memo[(i,buy)]
            elif (i==len(prices)):
                return 0
            elif (buy ==1):
                profit=-prices[i]+sp(i+1,0)
                skip=sp(i+1,1)
        
            elif(buy==0):
                profit=prices[i]-fee+sp(i+1,1)
                skip=sp(i+1,0)

            memo[(i,buy)]= max(profit,skip)
            return memo[(i,buy)]

            
        return  sp(0,1)