class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans=[["#"]*n for _ in range(m)]
        def reach(i,j):
            if i==m-1 and j==n-1:
                ans[i][j]="."
            else:
                ans[i][j]="."           
                if (i==m-1):
                    reach(i,j+1)
                else:
                    reach(i+1,j)
        reach(0,0)
        for i in range(m):
            ans[i]="".join(ans[i])
        
        return ans
