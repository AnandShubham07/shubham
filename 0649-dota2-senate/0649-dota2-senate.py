class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=[]
        d=[]
        l=len(senate)
        for i in range(0,l):
            if (senate[i]=="R"):
                r.append(i)
            else:
                d.append(i)
    
        while(r and d):
            if r[0]<d[0]:
                d.pop(0)
                r.append(r[0]+l)
                r.pop(0)
            else:
                r.pop(0)
                d.append(d[0]+l)
                d.pop(0)
        if r:
            return "Radiant"
        else:
            return "Dire"
            
            
        