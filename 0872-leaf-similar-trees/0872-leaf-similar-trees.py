# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        list1=[]
        list2=[]
        def dfs1(root1):
            if(root1!=None):
                if(root1.left==None and root1.right==None):
                    return root1.val
                l=dfs1(root1.left)
                if(l!=None):
                    list1.append(l)
                r=dfs1(root1.right)
                if(r!=None):
                    list1.append(r)
                return
        dfs1(root1)
        if(len(list1)==0):
            list1.append(root1.val)
        def dfs2(root2):
            if(root2!=None):
                if(root2.left==None and root2.right==None):
                    return root2.val
                l=dfs2(root2.left)
                if(l!=None):
                    list2.append(l)
                r=dfs2(root2.right)
                if(r!=None):
                    list2.append(r)
                return
        dfs2(root2)
        if(len(list2)==0):
            list2.append(root2.val)
        if(len(list1)!=len(list2)):
            return False
        # elif(len(list1)==len(list2)==0):
        #     if(root1.val!=root2.val):
        #         return False
        #     else:
        #         return True
        else:
            for i in range(0,len(list1)):
                if(list1[i]!=list2[i]):
                    return False
        return True


