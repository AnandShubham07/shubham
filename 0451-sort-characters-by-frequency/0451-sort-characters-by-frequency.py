class Solution:
    def frequencySort(self, s: str) -> str:
        dict={}
       
        for element in s:
            if element not in dict:
                dict[element] = 1         
            else:
                dict[element]=dict[element]+1

        new=""
        i=0
        k=len(dict)
        values=list(dict.values())
        items=list(sorted(dict.items()))
        while(i<k):
            c=max(values)
            for key,v in items:
                if(v==c):
                    new=new+key*v
                    break
            items.remove((key,v))
            values.remove(c)
            i=i+1
        return new
        