class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        queue=[]
        visited=set()
        adj=[[] for _ in range (n)]
        for u,v,w in edges :
            adj[u].append((v,w))

        queue.append((0,0,labels[0],1))
        # visited.add((0,labels[0],1))
        while(queue):
            queue.sort()
            
            dist,node,lastchar,count=queue.pop(0)
            state=(node,lastchar,count)
            if state in visited:
                continue
            visited.add(state)

            if node==n-1:
                return dist

            for nei,weight in adj[node]:               
                new_char=labels[nei]
                if (new_char==lastchar):
                    new_count=count+1
                else:
                    new_count=1
                
                if new_count<=k:
                    new_state=(nei,new_char,new_count)

                    if new_state not in  visited:
                        queue.append((dist+weight,nei,new_char,new_count))
            
        return -1

