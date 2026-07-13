# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        levels = []
        def dfs(node,depth):
            if not node:
                return
            if depth == len(levels):
                res.append(node.val)
                levels.append([])
            levels[depth].append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root,0)
        return res


