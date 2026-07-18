# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        left_max, right_min = float('inf'), float('-inf')
        def dfs(root,left_max,right_min):
            if not root:
                return True
            if root.val >= left_max:
                return False
            if root.val <= right_min:
                return False
            left_path = dfs(root.left, min(root.val,left_max),right_min)
            right_path = dfs(root.right,left_max,max(right_min,root.val))
            return left_path and right_path
        return dfs(root,left_max, right_min)