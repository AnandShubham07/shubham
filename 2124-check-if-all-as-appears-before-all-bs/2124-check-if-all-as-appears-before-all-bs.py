class Solution:
    def checkString(self, s: str) -> bool:
        curr_a=0
        curr_b=inf
        for i in range(0,len(s)):
            if s[i]=='b':
                curr_b=i
            else:
                curr_a=i
                if not (curr_a<=curr_b):
                    return False
        return True



        