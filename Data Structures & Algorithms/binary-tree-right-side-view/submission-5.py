# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightArray = []
        q = deque()
        if root:
            q.append(root)
        while q:
            LevelArray = []
            for i in range(len(q)):
                node = q.popleft()
                LevelArray.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            rightArray.append(LevelArray[-1])
        return rightArray
        