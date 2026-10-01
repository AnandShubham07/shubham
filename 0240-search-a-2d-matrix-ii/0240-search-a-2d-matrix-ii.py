class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        last=len(matrix[0])
        for i in range(0,m):
            for j in range(0,last):
                if(matrix[i][j]>target):
                  if(j==0):
                    return False
                  else:
                    last=j
                elif(matrix[i][j]==target):
                    return True
        return False
                
            
        