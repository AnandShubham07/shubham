# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,current):
            if(node!=None):               
                current.append(node.val)
                if(node.val==max(current)):
                    l.append(current)
                dfs(node.left,current)
                dfs(node.right,current)                
                
                
                current.pop()
                return  

        l=[]
        dfs(root,[])
        return(len(l))

