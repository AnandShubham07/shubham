class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def next_per(n,curr):
            for i in range(n-1,-1,-1):
                if(curr[i-1]<curr[i]):
                    index=i-1
                    break
                elif(i==1 or i==0):
                    return sorted(curr)
                
            for i in range(n-1,index,-1):
                if(curr[i]>curr[index]):
                    curr[i],curr[index]=curr[index],curr[i]
                    break
            curr[:]=curr[:index+1]+curr[:index:-1]
            return curr
        n=len(nums)
        nums.sort()
        copy=nums.copy()
        result=[copy]       
        while(1):           
            result.append(next_per(n,result[-1].copy()))
            if(result[-1]==copy):
                break
        result.pop()
        return result
            
