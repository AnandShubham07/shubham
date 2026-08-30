class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        left=0
        for i in range(0,l):
            for j in  range(left,l):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

            left=left+1
     
        for i  in range(0,l):
            for j in range(0,l//2):
                matrix[i][j],matrix[i][l-1-j]=matrix[i][l-1-j],matrix[i][j]
