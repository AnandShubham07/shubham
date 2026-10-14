# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        maximal=1
        def bfs(level,maxi,no):
            nonlocal maximal
            if not level :
                return 
            
            # s=0
            s=None
            next_level=[]
            for  node in level:
                if node.left:
                    if s is None:
                        s=node.left.val
                        next_level.append(node.left)
                    else:
                        s+=node.left.val
                        next_level.append(node.left)
                if(node.right):
                    if s is None:
                        s=node.right.val
                        next_level.append(node.right)
                    else:
                        s+=node.right.val
                        next_level.append(node.right)

            if(s is  not None):               
                if(s>maxi):
                    maxi=s 
                    maximal=no+1          
            bfs(next_level,maxi,no+1)

        bfs([root],root.val,1)
        return maximal

            