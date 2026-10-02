class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum=max(candies)
        n=len(candies)
        result=[]
        for i in range(0,n):
            if(candies[i]+extraCandies>=maximum):
                result.append(True)
            else:
                result.append(False)
        return result
        