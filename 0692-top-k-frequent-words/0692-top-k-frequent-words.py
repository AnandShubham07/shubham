class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict={}
        for element in words:
            if element not in dict:
                dict[element] = 1         
            else:
                dict[element]=dict[element]+1
        

        s=[]
        i=0
        values=list(dict.values())
        items=list(sorted(dict.items()))
        while(i<k):
            c=max(values)
            for key,v in items:
                if(v==c):
                    s.append(key)
                    break
            items.remove((key,v))
            values.remove(c)
            i=i+1
        return s


