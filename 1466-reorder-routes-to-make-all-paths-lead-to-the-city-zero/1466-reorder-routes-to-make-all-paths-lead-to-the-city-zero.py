class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        l=len(connections)
        visited={0}
        graph=[[] for _ in range(n)]
        
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))
        
        def dfs(i):
            visited.add(i)
            ans=0

            for j,cost in graph[i]:
                if j not in visited:
                    ans+=cost
                    ans+=dfs(j)
            return ans
        ans=dfs(0)
        return ans