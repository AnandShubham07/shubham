class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l=1
        n=len(board)
        m=len(board[0])
        visited=set()
        def dp(i,j,result,l):
                 
            if(result==word):
                return True
            if(len(result)>len(word)):
                return False   
            if(i>0):
                if((i-1,j) not in visited and board[i-1][j]==word[l]):
                    visited.add((i-1,j))
                    new_result=result+board[i-1][j]
                    if(dp(i-1,j,new_result,l+1)):
                       return True
                    visited.remove((i-1,j))
            if(j>0):
                if((i,j-1) not in visited and board[i][j-1]==word[l]):
                        visited.add((i,j-1))
                        new_result=result+board[i][j-1]
                        if(dp(i,j-1,new_result,l+1)):
                            return True
                        visited.remove((i,j-1))
            if(j+1<m):
                if((i,j+1) not in visited and board[i][j+1]==word[l]):  
                        visited.add((i,j+1))     
                        new_result=result+board[i][j+1]                
                        if(dp(i,j+1,new_result,l+1)):
                            return True
                        visited.remove((i,j+1))
            if(i+1<n):
                if((i+1,j) not in visited and board[i+1][j]==word[l]): 
                        visited.add((i+1,j))     
                        new_result=result+board[i+1][j]                
                        if(dp(i+1,j,new_result,l+1)):
                            return True
                        visited.remove((i+1,j))
            return False

        for i in range(0,n):
            for j in range(0,m):
                if (board[i][j] ==word[0]):
                    result=board[i][j]
                    visited.add((i,j))
                    if(dp(i,j,result,l)):
                        return True
                    visited.remove((i,j))
        return False



            