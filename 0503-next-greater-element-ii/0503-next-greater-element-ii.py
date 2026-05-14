class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        dict = {}

        n = len(nums)

        for i in range(2 * n - 1, -1, -1):

            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if not stack:
                dict[i % n] = -1
            else:
                dict[i % n] = stack[-1]

            stack.append(nums[i % n])

        ans = []

        for i in range(n):
            ans.append(dict[i])

        return ans
