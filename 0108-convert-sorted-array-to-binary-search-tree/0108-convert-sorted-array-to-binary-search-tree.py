# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary(left,right):
            if(left>right):
                return None
            mid=(left+right)//2
            result=TreeNode(nums[mid],None,None)
            result.left=binary(left,mid-1)
            result.right=binary(mid+1,right)
            return result
        return binary(0,len(nums)-1)
