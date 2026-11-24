import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=-inf
        for i in range(0,n):
            prod=1
            lcm=1
            hcf=0
            for j in range(i,n):
                prod*=nums[j]
                lcm=math.lcm(lcm,nums[j])
                hcf=math.gcd(hcf,nums[j])
                if prod==lcm*hcf:
                    length=j-i+1
                    if maxi<length:
                        maxi=length
        return maxi
