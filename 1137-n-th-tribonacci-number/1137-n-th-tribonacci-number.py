class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def tri(n):
            if n in memo:
                return memo[n]
            if (n==1 or n==2):
                memo[n]=1
                return memo[n]
            elif(n==0):
                memo[0]=0
                return memo[0]
            else:
                memo[n]=(tri(n-1) +tri(n-2) +tri(n-3))
                return memo[n]
        return tri(n)
        