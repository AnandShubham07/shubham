class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=[]
        left=0
        right=len(numbers)-1
        while(left<right):
            if(numbers[left]+numbers[right]==target):
                l.append(left+1)
                l.append(right+1)
                return l
            elif(numbers[left]+numbers[right]<target):
                left+=1
            else:
                right-=1
