class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid[0])
        n=len(obstacleGrid)
        result=[[-1]*m for _ in range(n)]
        # if(obstacleGrid[n-1][m-1]==1):
        #     return 0
        def dp(i,j):
                if(i<0 or j<0 ):
                    return 0
                if(obstacleGrid[i][j]==1):               
                    return 0
                if(i==0 and j==0):
                    return 1
                if( result[i][j]!=-1):
                    return result[i][j]
                if(i>0 or j>0):
                    result[i][j]=dp(i,j-1)+dp(i-1,j)
                return result[i][j]
        
        return dp(n-1,m-1)
                
                    