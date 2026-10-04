class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        r={}
        c={i:[] for i in range(0,len(grid))}
        for i in range(0,len(grid)):
            r[i]=grid[i]
        for i in range(0,len(grid)):
            for j in range(0,len(grid)):
                c[j].append(grid[i][j])
        count=0
        for k in range(0,len(grid)):
            for j in range(0,len(grid)):
                if(r[k]==c[j]):
                    count+=1
        return count


        