class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        vowels=['a','e','i','o','u']
        new=""
        maxi=0
        for i in range(0,k):
            new+=s[i]
            if(s[i] in vowels):
                maxi+=1
        count=maxi
        for i  in range(k,n):
            last=s[i]
            first=s[i-k]
            if(first in vowels):
                count-=1
            new+=last
            if(last in vowels):
                count+=1
            if(count>maxi):
                maxi=count
        return maxi




            
        