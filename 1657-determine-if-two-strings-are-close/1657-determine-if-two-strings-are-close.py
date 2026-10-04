class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!= len(word2)):
            return False
        d1={}
        d2={}
        for i in range(0,len(word1)):
            if word1[i] not in d1:
                d1[word1[i]]=1
            else:
                d1[word1[i]]+=1
        
        for i in range(0,len(word2)):
            if word2[i] not in d2:
                d2[word2[i]]=1
            else:
                d2[word2[i]]+=1
        for elements in d1:
            if(elements  not in d2):
                return False
        for elements in d2:
            if(elements not in d1):
                return False
        s1=[sorted([value for value in d1.values() ])]
        s2=[sorted([value for value in d2.values() ])]
        for i in range(0,len(s1)):
            if(s1[i]!= s2[i]):
                return False
        return True
        
            
        
        