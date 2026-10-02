class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        s=""
        while(i<len(word1) or j<len(word2)):
            if(i<len(word1) and j<len(word2)):
                s+=word1[i]
                s+=word2[j]
            elif(i>=len(word1) and j<len(word2)):
                s+=word2[j]
            elif(i<len(word1) and j>=len(word2)):
                s+=word1[j]
            i+=1
            j+=1
        return s





        