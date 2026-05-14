class Solution:
    def isValid(self, s: str) -> bool:

        list=[]
        dict={'(':')','{':'}','[':']'}
        def stack(c):
           
            if c in dict:
                list.append(c)
            else:
                if not list:
                    return False

                if c==dict[list[-1]]:
                    list.pop()
                else:
                    return False
            return True
            
           
        for i in range(0,len(s)):
           if stack(s[i]) == False:
            return False
       
        return len(list) == 0