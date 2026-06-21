# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if abs(left_height - right_height) > 1 or (left_height == -1 or right_height == -1):
                flag[0] = False
                return -1

            return 1 + max(left_height,right_height) if flag[0] else -1

        dfs(root)
        return flag[0]
        