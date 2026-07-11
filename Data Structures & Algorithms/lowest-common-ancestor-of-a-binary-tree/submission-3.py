# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return 
            if node == p:
                return node
            if node == q:
                return node
            
            left,right = dfs(node.left), dfs(node.right)

            if left and right:
                return node
            else:
                return left or right

        return dfs(root)