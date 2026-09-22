class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        check=set()
        for i in nums:
            if i in check:
                return True
            if i not in check:
                check.add(i)
        return False
            
        