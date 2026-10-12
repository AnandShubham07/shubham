# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def bfs(level):
            if not level:
                return  
            next_level=[]
            for node in level:               
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            l.append(level[-1].val)
            bfs(next_level)
        if root is None:
            return []
        l=[]
        bfs([root])
        return l
            
                


           



        