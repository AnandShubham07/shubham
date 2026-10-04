class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[asteroids[0]]
        for i in range(1,len(asteroids)):
            stack.append(asteroids[i])
            while(len(stack)>1 and stack[-2]>0 and stack[-1]<0):
                if(abs(stack[-1])>abs(stack[-2])):
                    s=stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(s)
                elif(abs(stack[-1])==abs(stack[-2])):
                    stack.pop()
                    stack.pop()
                else:
                    stack.pop()
                    break
            
        return stack

        