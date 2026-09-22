class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        visited=list()
        for i in nums:
            if (i+0.5) in visited:
                visited.remove(i+0.5)
            elif i not in visited:
                visited.append(i)
            else: 
                visited.remove(i)
                visited.append(i+0.5)
        return visited[0]

        