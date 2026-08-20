class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       
        incr=0
        d=len(digits)
        for i in range(0,d):
            incr=incr+10**(d-(i+1))*digits[i]
        incr+=1
        n=len(str(incr))
        new=[]
        for i in range(n-1,-1,-1):
            new.append(incr//10**i)
            incr=incr % (10**i)
        return new
        