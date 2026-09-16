class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        numrows=rowIndex
        def multiple(p1,p2):
            result=[0]*(len(p1)+len(p2)-1)

            for i in range(0,len(p1)):
                for j in range(0,len(p2)):
                    result[i+j]+=p1[i]*p2[j]

            return result
        if(numrows==0):
            return [1]
        new=[1,1]
        x=[1,1]
        while(numrows>1):
            new=multiple(new,x)
            numrows-=1
        return new


        

        