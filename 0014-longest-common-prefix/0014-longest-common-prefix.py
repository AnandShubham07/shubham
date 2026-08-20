class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if not strs:
            return ""
        left=0
        right=n-1
        while(left<right):
            prefix_length=0
            for i in range(0,min(len(strs[left]),len(strs[right]))):
                if(strs[left][i]==strs[right][i] ):
                    prefix_length+=1
                        
                else:
                    break
            right=right-1 
            strs[left]=strs[left][0:prefix_length]
                   
        return strs[left]
        
                
    
        



        