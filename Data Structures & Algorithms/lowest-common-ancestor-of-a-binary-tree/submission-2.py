# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_list = []
        q_list = []

        def find_p(node, node_list):
            if not node:
                return False
            if node == p:
                node_list.append(node)
                p_list.extend(node_list)
                return True
            node_list.append(node)
            left_path = find_p(node.left, node_list)
            if left_path:
                return True
            right_path = find_p(node.right, node_list)
            if right_path:
                return True
            node_list.pop()
        
        def find_q(node, node_list):
            if not node:
                return False
            if node == q:
                node_list.append(node)
                q_list.extend(node_list)
                return True
            node_list.append(node)
            left_path = find_q(node.left, node_list)
            if left_path:
                return True
            right_path = find_q(node.right, node_list)
            if right_path:
                return True
            node_list.pop()
        
        find_p(root, [])
        find_q(root, [])

        
        if len(p_list) > len(q_list):
            q_list = set(q_list)
            while p_list:
                node = p_list.pop()
                if node in q_list:
                    return node
        else:
            p_list = set(p_list)
            while q_list:
                node = q_list.pop()
                if node in p_list:
                    return node

        