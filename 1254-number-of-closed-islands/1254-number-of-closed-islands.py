class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j):
            
            if(i<0 or j<0 or i>=m or j>=n):
                return False

            if (i,j) in visited :
                return True

            if (grid[i][j]==1):
                visited.add((i,j))
                return True
            
            visited.add((i,j))

            surrounded=not(i==0 or j==0 or i==m-1 or j==n-1)
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            return surrounded and  up and down and left and right
        
        count=0
        for i in range(0,m):
            for j in range(0,n):
                if (grid[i][j] ==0 and (i,j) not in visited ):
                    if dfs(i,j):
                        count+=1
        return count
                
        