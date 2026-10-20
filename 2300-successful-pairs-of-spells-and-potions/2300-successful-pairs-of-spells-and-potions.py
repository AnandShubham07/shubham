class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:


        potion=sorted(potions)
        pairs=[]
        for i in range(len(spells)):
            left=0
            right=len(potion)-1
            pair=0
            while(left<=right):
                mid=(left+right)//2
                if(potion[mid]>=success/spells[i]):
                    pair=len(potion)-mid
                    right=mid-1
                else:
                    left=mid+1
            pairs.append(pair)
        return pairs
                