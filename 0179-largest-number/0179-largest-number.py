from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(a,b):
            if str(a)+str(b)>=str(b)+str(a):
                return -1
            else:
                return 1
        nums.sort(key=cmp_to_key(cmp))
        result= "".join(str(x) for x in nums)
        return "0" if result[0]=="0" else result

