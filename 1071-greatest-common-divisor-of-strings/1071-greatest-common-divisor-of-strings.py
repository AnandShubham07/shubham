class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i=0
        gcd=""
        s=""
        ans=""
        if(len(str1)==0 or len(str2)==0):
            return ""
        while(i<len(str1) and i<len(str2)):
            if(str1[i]==str2[i]):
                s+=str1[i]
                i+=1
            else:
                return ""

        for j in range(0,len(s)):
            gcd+=s[j]
            mul1=len(str1)//len(gcd)
            mul2=len(str2)//len(gcd)
            if(gcd*mul1==str1 and gcd*mul2==str2 ):
                ans=gcd

        return ans

        
        

        