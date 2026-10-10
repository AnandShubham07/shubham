# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,p,q):
            if(node==None):
                return 
            else:
                if(node==p):
                   return node
                elif(node==q):
                    return node
                left=dfs(node.left,p,q)
                right=dfs(node.right,p,q)
                if(left is not None and right is not None):
                    return node
                elif(left is not None):
                    return left
                else:
                    return right

        return (dfs(root,p,q))
        
    