class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letter=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        digit=[int(i) for i in digits]
        ans=[]
        m=len(digits)
        def dfs(i,current):
            if(i==m):
                ans.append("".join(current.copy()))
            if (i>=m):
                return 
            for j in range(0,len(letter[digit[i]])):
                current.append(letter[digit[i]][j])
                dfs(i+1,current)
                current.pop()
        dfs(0,[])
        return ans


        