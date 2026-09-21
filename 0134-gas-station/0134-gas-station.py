class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n=len(gas)
        total,result=0,0
        fuel=0
        start=[]
        for i in range(0,n):
            start.append(gas[i]-cost[i])

            total+=start[i]
            fuel+=start[i]
            if(fuel<0):
                result=i+1
                fuel=0

        if(total<0):
            return -1
        else:
            return result
            
                



        