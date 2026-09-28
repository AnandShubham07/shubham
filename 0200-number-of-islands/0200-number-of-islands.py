class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        visited=set()
        def dfs(i,j,region):
            if(i<0 or j<0 or i>m-1 or j>n-1):
                return True
            if(grid[i][j]=="0" or (i,j) in visited):
                return True
            
            visited.add((i,j))
            region.append((i,j))
            top=dfs(i-1,j,region)
            down=dfs(i+1,j,region)
            left=dfs(i,j-1,region)
            right=dfs(i,j+1,region)
            
            return top and down and left and right
        
        for i in range(0,m):
            for j in range(0,n):
                if(grid[i][j]=="1"  and (i,j) not in visited):
                    region=[]
                    if(dfs(i,j,region)):
                        count+=1
        return count
        