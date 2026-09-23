class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        n=len(tokens)
        operations=["+","*","-","/"]
        l=[]
        for i in range(0,n):
            if tokens[i] not in operations:
                l.append(int(tokens[i]))
            else:
                if tokens[i]=="+":
                    l.append(int(l.pop()+l.pop()))
                elif tokens[i]=="-":
                    l.append(int(l.pop()-l.pop())*-1)
                elif tokens[i]=="*":
                    l.append(int(l.pop()*l.pop()))
                else:
                    s=l.pop()
                    f=l.pop()
                    l.append(int(f/s))
        return l[0]


        