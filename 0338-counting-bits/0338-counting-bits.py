class Solution:
    def countBits(self, n: int) -> list[int]:
        ans=[]
        for i in range(0,n+1):
            res=0
            while(i>0):
                if(i%2==1):
                    res+=1
                i=i//2
            ans.append(res)
        return ans
        