class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c=0
        def isduplicate(arr):
            nums=[]
            for i in range(0,9):
                if(arr[i]=="."):
                    continue
                if(arr[i] not in nums):
                    nums.append(arr[i])
                else:
                    return True
            return False
        for i  in  range(0,9):
            if (isduplicate(board[i])):
                return False
        while(c<9):
            arr=[]
            for i in range(len(board)):
                arr.append(board[i][c])
            if(isduplicate(arr)):
                return False
            else:
                c=c+1
        
        
        r,c=0,0
        k=0
        while(c<9):
            new=[]           
            for  i in range(r,r+3):
                for j in range(k,k+3):
                        new.append(board[i][j])
                k=(c%3)*3
            if(isduplicate(new)):
                return False
            c=c+1
            r=(c//3)*3
            k=(c%3)*3
           
        return True

            
