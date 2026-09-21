class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        visited=set()
        for  i in nums:
            if i not in visited:
                visited.add(i)
            else:
                visited.remove(i)

        for x in visited:
            return x

        