class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent=list(range(len(isConnected)))
        n=len(isConnected)
        def find(x):
            return parent[x]
        def union(x,y):
            root_x=find(x)
            root_y=find(y)

            for i in range(0,n):
                if(parent[i]==root_y):               
                    parent[i]=root_x
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if(isConnected[i][j]==1):
                    union(i,j)
        group=set(parent)
        return len(group)
                
        