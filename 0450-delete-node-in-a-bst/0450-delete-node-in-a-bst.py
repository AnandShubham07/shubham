# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def delete(node,key):
            if(node==None):
                return
            elif(node.val<key):
                node.right=delete(node.right,key)
            elif(node.val>key):
                node.left=delete(node.left,key)
            else:
                if(node.left==None):
                    if(node.right==None):
                        return
                    else:
                        return node.right
                elif(node.right==None):
                    return node.left
                else:
                    ptr=node
                    node=node.left
                    while(node.right!=None):
                        node=node.right
                    ptr.val=node.val
                    ptr.left=delete(ptr.left,ptr.val)
                return ptr
            return node
            
        root=delete(root,key)
        return root
              


        