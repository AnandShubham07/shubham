class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        al,bl,cl=[],[],[]
        def places(n,l):
            while(n!=0):
                l.append(n&1)
                n=n>>1
        places(a,al)
        places(b,bl)
        places(c,cl)
        flip=0
        m,n,o=len(al),len(bl),len(cl)
        maxi=max(m,n,o)
        al+=[0]*(maxi-m)
        bl+=[0]*(maxi-n) 
        cl+=[0]*(maxi-o)      
        for i in range(0,maxi):            
            if (al[i] | bl[i])!=cl[i]:
                if (cl[i]==1):
                    flip+=1
                else:
                    if(al[i] & bl[i]==1):
                        flip+=2
                    else:
                        flip+=1
        return flip



                