class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n=len(rating) 
        result=0
        for i in range(0,n):
            leftlarger=leftsmaller=0
            rightlarger=rightsmaller=0
            for j in range (i+1,n):
                if(rating[i]>rating[j]):
                    rightsmaller+=1
                elif(rating[i]<rating[j]):
                    rightlarger+=1
            for k in range(0,i):
                if(rating[i]>rating[k]):
                    leftsmaller+=1
                elif(rating[i]<rating[k]):
                    leftlarger+=1
            increasing=leftsmaller*rightlarger
            decreasing=rightsmaller*leftlarger
            result+=increasing+decreasing
        return result
        
    


        



