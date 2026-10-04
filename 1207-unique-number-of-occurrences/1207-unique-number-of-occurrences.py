class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d={}
        n=len(arr)
        for i in range(0,n):
            if(arr[i] not in d ):
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        values=[value for value in d.values()]
        new=sorted(values)
        for i in range(1,len(new)):
            if(new[i-1]==new[i]):
                return False
        return True

        