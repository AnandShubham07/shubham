class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def divide(s,k):
            ans=""
            final=""
            for ch in s:
                ans+=ch
                if (len(ans)==k):
                    final+=str(replace(ans))
                    ans=""
            if ans:
                final+=str(replace(ans))
            return final
        def replace(ans):
            s=0
            for elem in ans:
                s+=int(elem)
            return s
        
        while len(s) > k:
            s = divide(s, k)

        return s