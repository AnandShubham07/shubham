class Solution:
    def compress(self, chars: list[str]) -> int:
        i=1
        s=""+chars[0]
        count=1
        while(i<len(chars)):
            if(chars[i]==chars[i-1]):
                count+=1
                i+=1               
            else:
                if(count!=1):
                    s+=str(count)
                s+=chars[i]
                count=1
                i+=1
        if count!=1 :
            s+=str(count)
        for j in range(0,len(s)):
            chars[j]=s[j]
        return len(s)
        