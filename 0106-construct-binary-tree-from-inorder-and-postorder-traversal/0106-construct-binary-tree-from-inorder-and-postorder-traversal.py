# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_index=len(postorder)-1
        def traversal(left,right):
            nonlocal post_index
            if(left>right):
                return None
            result=TreeNode(postorder[post_index],None,None)
            post_index-=1
            result_index=inorder.index(result.val)
            
            result.right=traversal(result_index+1,right)
            result.left=traversal(left,result_index-1)
            
            return result
        return traversal(0,len(inorder)-1)



        