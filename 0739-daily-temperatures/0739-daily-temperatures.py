class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temp=temperatures
        n=len(temp)
        ans=[0]*n
        stack=[]
        for i in range(0,len(temp)):        
                while(stack and temp[stack[-1]]<temp[i]):
                    ans[stack[-1]]=i-stack[-1]
                    stack.pop()
               
                stack.append(i)
        return ans

