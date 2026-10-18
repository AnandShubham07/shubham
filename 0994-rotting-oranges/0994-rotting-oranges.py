class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        fresh=0
        queue=[]
        for i in range(0,m):
            for j in range(0,n):
                if(grid[i][j]==2):
                    queue.append((i,j))
                elif(grid[i][j]==1):
                    fresh+=1
        minutes=0
        while(queue):
            size=len(queue)
            found=0
            for r in range(size):
                i,j=queue.pop(0)
                up,down,left,right=0,0,0,0
                
                if(i-1>=0):
                    up=grid[i-1][j]
                if(i+1<m):
                    down=grid[i+1][j]
                if(j-1>=0):
                    left=grid[i][j-1]
                if(j+1<n):
                    right=grid[i][j+1]

                if up==1:
                    grid[i-1][j]=2
                    queue.append((i-1,j))
                    fresh-=1
                    found=1
                if down==1:
                    grid[i+1][j]=2
                    queue.append((i+1,j))
                    fresh-=1
                    found=1
                if left==1:
                    grid[i][j-1]=2
                    queue.append((i,j-1))
                    fresh-=1
                    found=1
                if right==1:
                    grid[i][j+1]=2
                    queue.append((i,j+1))
                    fresh-=1
                    found=1

                
            if(found==1):
                minutes+=1

        if fresh>0:
            return -1
        else:
            return minutes


        