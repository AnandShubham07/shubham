class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        visited=set()
        def dfs(i,j,region):
            if(i<0 or i>=m or j<0 or j>=n):
                return False
            if(board[i][j]=="X" or (i,j) in visited ):
                    return True
            visited.add((i,j))
            region.append((i,j))           

            if(i==m-1 or j==n-1 or i==0 or j==0):
                surrounded=False
            else:
                surrounded=True
            top=dfs(i-1,j,region)  
            down=dfs(i+1,j,region)  
            left=dfs(i,j-1,region)  
            right=dfs(i,j+1,region)   
            return surrounded and top and down and left and right   
        for i in range(0,m):
            for  j in range(0,n):
                if(board[i][j]=="O" and (i,j) not in visited ):
                    region=[]
                    if(dfs(i,j,region)):
                        for (x,y) in region:
                            board[x][y]="X"