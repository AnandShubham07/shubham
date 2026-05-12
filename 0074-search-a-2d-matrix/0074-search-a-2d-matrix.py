class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)*len(matrix[0])-1
         
        while(low<=high):    
            mid=(low+high)//2
            i=mid // len(matrix[0])
            j=mid %len(matrix[0]) 

            if(matrix[i][j]==target):
                return True
            elif(matrix[i][j]<target):
                low=mid+1
            else:
               high=mid-1
            
        return False 