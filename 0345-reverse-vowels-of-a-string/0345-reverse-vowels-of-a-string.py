class Solution:
    def reverseVowels(self, s: str) -> str:
        str1=""
        rem=[]
        vowels=["a","e","i","o","u"]
        for i  in range(0,len(s)):
            if(s[i].lower() in vowels):
                rem.append(s[i])
        for i in range(len(s)):
            if(s[i].lower() in vowels):
                str1+=rem[-1]
                rem.pop()
            else:
                str1+=s[i]
        return str1
        