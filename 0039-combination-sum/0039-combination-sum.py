class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        current=[]
        result=[]
        def dfs(start,target,current):
            if(sum(current)==target):
                result.append(current.copy())
            elif(sum(current)>target):
                return
            for i in range(start,n):
                current.append(candidates[i])
                dfs(i,target,current)
                current.pop()
        dfs(0,target,current)
        return result
        
            

        