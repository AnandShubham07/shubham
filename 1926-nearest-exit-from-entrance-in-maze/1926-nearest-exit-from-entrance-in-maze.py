class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m=len(maze)
        n=len(maze[0])

        visited=[[False]*n for _ in range(m)]
        i,j=entrance[0],entrance[1]
        queue=[(i,j,0)]
        front=0
        mini=float("inf")
        visited[i][j]=True

        while(front <len(queue)):
            r,c,count=queue[front]
            front+=1
            
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if (nr<0 or nc<0 or nr>=m or nc>=n):
                    continue                
                if(maze[nr][nc]=="+" or visited[nr][nc]):
                    continue
                if (nr==0 or nr==m-1 or nc==0 or nc==n-1):
                    return count+1

                visited[nr][nc]=True                       
                queue.append((nr,nc,count+1))
        return -1
                
        