class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        target=n
        def backtrack(start,target,current):
            if(sum(current)==target and len(current)==k):
                result.append(current.copy())
                return 
            elif(sum(current)>target or len(current)>=k):
                return 
            else:
                for i  in range(start,10):
                    current.append(i)
                    backtrack(i+1,target,current)
                    current.pop()
        backtrack(1,target,[])
        return result
        
            