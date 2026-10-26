class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j):
            if (i<0 or j<0 or i>=m or j>=n):
                return 0

            if(grid[i][j]==0):
                return 0

            total=grid[i][j]
            grid[i][j]=0

            up=dfs(i-1,j)
            down =dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)

            return (total+up+down+left+right)

        count=0
        for i in range(0,m):
            for j in range(0,n):
                if (grid[i][j]!=0):
                    total_value=dfs(i,j)
                    if (total_value%k==0):
                        count+=1
        return count

                
            
        