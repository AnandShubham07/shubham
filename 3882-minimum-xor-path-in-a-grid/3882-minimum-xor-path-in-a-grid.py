class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        memo=[[-1]*n for _ in range(m)]
        def dfs(i,j):
            if (memo[i][j]!=-1):
                return memo[i][j]
            
            if (i==0 and j==0):
                memo[i][j]=1<<grid[i][j]
                return memo[i][j]
            
            else:
                prev=0
                if (i>0):
                    prev|= dfs(i-1,j)

                if(j>0):
                    prev|=dfs(i,j-1)
                
                x=grid[i][j]
                mask=0
                while prev:
                    bit=prev&-prev
                    prev=prev^bit 
                    v=bit.bit_length()-1
                    mask|=1<<(v^x)
                memo[i][j]=mask
                return memo[i][j]
            
        mask=dfs(m-1,n-1)
        return (mask&-mask).bit_length()-1

