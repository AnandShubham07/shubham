# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p_index=0
        def traversal(instart,inend):
            nonlocal p_index
            if(instart>inend):
                return None
            root_val=preorder[p_index]
            p_index=p_index+1
            root=TreeNode(root_val,None,None)
            # root_index=inorder[instart:inend].index(root_val)
            for j in range(instart,inend+1):
                if(inorder[j]==root_val):
                    root_index=j
                    break
            root.left=traversal(instart,root_index-1)
            root.right=traversal(root_index+1,inend)
            return root
        return traversal(0,len(inorder)-1)
            
