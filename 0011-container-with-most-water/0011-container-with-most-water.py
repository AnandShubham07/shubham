class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        curr=0
        while(low<high):
            if(height[low]<height[high]):
                area=height[low]*(high-low)
                curr=max(area,curr)
                low=low+1
            else:
                area=height[high]*(high-low)
                curr=max(area,curr)
                high=high-1
           
        return curr
            
            
        
        