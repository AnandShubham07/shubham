class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        memo={}
        def dp(i,j):
            if(i==0 and j==0):
                memo[(i,j)]=grid[0][0]
                return  memo[(i,j)]
            if(i==0):
                return grid[i][j]+dp(i,j-1)
            if(j==0):
                return grid[i][j]+dp(i-1,j)
            
            if(i,j) in memo:
                return memo[(i,j)]

            if(i>0 and j>0):
                 memo[(i,j)]=grid[i][j]+min(dp(i-1,j),dp(i,j-1))
            return memo[(i,j)]
        
        return dp(n-1,m-1)
        

        