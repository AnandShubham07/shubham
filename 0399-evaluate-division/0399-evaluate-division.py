class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        i=0
        for u,v in equations:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append((v,values[i]))
            graph[v].append((u,1/values[i]))
            i+=1

        def dfs(graph,start,end,visited):
            if(start==end):
                return 1
            visited.add(start)
            for j,val in graph.get(start,[]):
                if j not in visited:
                    result=dfs(graph,j,end,visited)
                    if(result!=-1):
                        return val*result
            return -1
        ans=[]
        for a,b in queries:
            if(a not in graph):
                ans.append(-1)
                continue
            ans.append(dfs(graph,a,b,set()))
        return ans


        