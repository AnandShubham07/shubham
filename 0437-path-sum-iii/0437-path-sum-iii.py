# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def dfs(node,pfsum,d):
            if(node==None):
                return 0
            else:
                pfsum+=node.val
                target=pfsum-targetSum
                count=0
                if(target in d):
                    count+=d[target]
                d[pfsum]=d.get(pfsum,0)+1
                count+=dfs(node.left,pfsum,d)
                count+=dfs(node.right,pfsum,d)

                d[pfsum]-=1
                pfsum-=node.val
                return count
        c=dfs(root,0,{0:1})
        return c



        # def prefix_sum(arr,targetSum):
        #     d={0:1}
        #     count=0
        #     prefix=0
            
        #     for num in arr:
        #         prefix+=num
        #         target=prefix-targetSum
        #         if(target) in d:
        #             count+=d[target]
        #         d[prefix]=d.get(prefix,0)+1
        #     return count
        
        # tcount=0
        # for i in range(0,len(list1)):
        #     c=prefix_sum(list1[i],targetSum)
        #     tcount+=c
        # return tcount



        