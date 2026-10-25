class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        l=[0]*num
        total=0
        for i in range(0, num):
            l[i]=9
            total+=l[i]
            while(total>sum):
                    l[i]-=1
                    total-=1
            if (total==sum):
                break
            
        if total!=sum:
            return ""
        return "".join(map(str,l))

        