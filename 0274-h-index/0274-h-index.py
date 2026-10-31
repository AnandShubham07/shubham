class Solution:
    def hIndex(self, citations: list[int]) -> int:
        maxi=0
        n=len(citations)
        citations.sort()
        for i in range(0, n):
            if citations[i]>=(n-i):
                if n-i>maxi:
                    maxi=n-i
        
        return maxi
        