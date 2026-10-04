class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=""
        str1=""
        for i in range(0,len(s)):
            stack.append(s[i])
            if(s[i]==']'):
                stack.pop()
                while(len(stack)!=0):
                    if(stack[-1]!='['):
                        str1+=stack[-1]
                        stack.pop()
                    else:
                        stack.pop()
                        break
                while(len(stack)!=0 and stack[-1].isdigit()):
                            num=num+stack[-1]                    
                            stack.pop()
                            continue
                  
                new=str1[::-1]
                digit=int(num[::-1])
                stack.extend(new*(digit))
                str1=""
                num=""
        return "".join(elem for elem in stack)



        