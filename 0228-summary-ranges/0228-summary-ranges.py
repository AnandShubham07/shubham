class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n=len(nums)
        if(n==0):
            return []
        a=nums[0]
        arr=[]
        b=nums[0]
        for i in range(1,n):
            if(nums[i]==nums[i-1] or nums[i]== nums[i-1]+1):
                b+=1
            else:
                arr.append([a,b])
                a=nums[i]
                b=nums[i]
        arr.append([a,b])
        for i in range(0,len(arr)):
            
                if(arr[i][0]==arr[i][1]):
                    arr[i]=str(arr[i][0])
                else:
                    arr[i]=str(arr[i][0])+"->"+str(arr[i][1])
        return arr
                

            


        