class Solution:
    def numTilings(self, n: int) -> int:
        memo={}
        mod =10**9 +7
        def tiles(n):
            if(n in memo):
                return memo[n]
            elif(n==0):
                return 1
            elif(n==1):
                return 1
            elif(n==2):
                return 2
            else:
                memo[n]=((2*tiles(n-1)+tiles(n-3))%mod)
                return memo[n]
        return(tiles(n))
        