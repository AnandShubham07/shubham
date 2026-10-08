class Solution:
    def reverseVowels(self, s: str) -> str:
        dict1={}
        n=""
        j=0
        vowels=set("aeiou")
        for i in range(0,len(s)):
            if(s[i].lower() in vowels):
                j+=1
                dict1[j]=s[i]
                           
        for i in range(0,len(s)):
            if(s[i].lower() in vowels):
                n+=dict1[j]
                j-=1
            else:
                n+=s[i]
        return n
