# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        maxi=0
        def dfs(root,count):
            nonlocal maxi
            if(root==None):
                return 
            count+=1           
            dfs(root.left,count)
            dfs(root.right,count)

            if(count>=maxi):
                maxi=count
            return
        dfs(root,0)
        return maxi
            

        