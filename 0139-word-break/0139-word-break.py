class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo={}
        def check(i,n):
            if(i==n):
                return True
            if(i,n)in memo:
                return memo[(i,n)]
            start=i
            new=""
            while(i!=n):
                new=new+s[i]
                if new in wordDict:
                    if check(i+1,n):
                        memo[(i,n)]=True
                        return True

                    
                i+=1
            memo[(start,n)]=False
            return False
        return check(0,len(s))

        