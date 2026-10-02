class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i=0
        l=len(flowerbed)
        if(l==1):
            return False if flowerbed[0]==1 and n==1 else True
        while (i<l):
            if(n==0):
                break
            if(flowerbed[i]==1):
                i+=2
            else:
                if((i==0  and flowerbed[1]==0) or (i==l-1 and flowerbed[l-2]==0)):
                    n-=1
                    i+=2
                elif(flowerbed[i-1]==flowerbed[i+1]==0):
                    n-=1
                    i+=2
                else:
                    i+=1
        if(n==0):
            return True
        else:
            return False


        