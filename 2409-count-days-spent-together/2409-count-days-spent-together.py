class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        ar=list(map(int,arriveAlice.split("-")))
        al=list(map(int,leaveAlice.split("-")))

        br=list(map(int,arriveBob.split("-")))
        bl=list(map(int,leaveBob.split("-")))

        m=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ps=[0,31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


        aA=ps[ar[0]-1]+ar[1]
        lA=ps[al[0]-1]+al[1]
        aB=ps[br[0]-1]+br[1]
        lB=ps[bl[0]-1]+bl[1]

        if (aA>lB):
            return 0
        elif (lA<aB):
            return 0
        else:      
            if(aB<aA):
                if(lB<lA):
                    return lB-aA+1
                else:
                    return lA-aA+1
            else:
                if (lA<lB):
                    return lA-aB+1
                else:
                    return lB-aB+1
                        
            
            