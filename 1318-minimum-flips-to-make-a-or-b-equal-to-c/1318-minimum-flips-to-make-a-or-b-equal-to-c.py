class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip=0
        while(a or b or c):   # a!=0 or b!=0 or c!=0
            x,y,z=a&1,b&1,c&1
                     
            if (x|y!=z):
                if (z==1):
                    flip+=1
                else:
                    if(x&y==1):
                        flip+=2
                    else:
                        flip+=1
            a=a>>1
            b=b>>1
            c=c>>1
        return flip