class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result=0
        for i in range(0,32):
            count=0
            for num in nums:
                count=count+((num>>i)&1 )   
            bit=count%3
            result|=(bit<<i)
        if(result>=2**31):
           result -= 2**32
        return result



        