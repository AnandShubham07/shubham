class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def pascal(nums):
            n=len(nums)-1
            arr=[nums[0]]
            if(n==0):
                arr.append(nums[0])
                return arr
            else:
                left=0
                right=left+1
                while(left<right):
                    if(left==n and right==n):
                        break
                    arr.append(nums[left]+nums[right])
                    if(left!=n):
                        left=left+1
                    if(right!=n):
                        right=right+1
                arr.append(1)    
                return arr
        arr=[[1]]
        for i in range(0,numRows-1):
            arr.append(pascal(arr[-1]))
        return arr

        