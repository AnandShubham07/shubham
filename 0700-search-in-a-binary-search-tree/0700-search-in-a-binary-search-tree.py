# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        new_node=None
        def dfs(node,val):
            nonlocal new_node
            if(node!=None):
                if(node.val==val):
                    new_node=node
                else:
                    dfs(node.left,val)
                    dfs(node.right,val)
                return
        dfs(root,val)
        return new_node
        