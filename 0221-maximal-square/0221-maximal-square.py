class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        ans=0
        memo={}
        def dp(i,j):
            if(i<0 or j<0 or i>=m or j>=n):
                return 0
            elif(i,j) in memo:
                return memo[(i,j)]
            elif(matrix[i][j]=="0"):
                memo[(i,j)]=0
                return memo[(i,j)]
            else:
                down=dp(i+1,j)
                right=dp(i,j+1)
                dia=dp(i+1,j+1)
                result=1+(min(down,right,dia))
                memo[(i,j)]=result
                return memo[(i,j)]

        for i in range(0,m):
            for j in range (0,n):
                ans=max(ans,dp(i,j))
        return ans*ans    
        
        