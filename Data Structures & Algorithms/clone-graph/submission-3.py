"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        stack = deque([node])
        node_to_copy = {node: Node(node.val)}
        while stack:
            curr = stack.popleft()
            for nei in curr.neighbors:
                if nei not in node_to_copy:
                    node_to_copy[nei] = Node(nei.val)
                    stack.append(nei) 
                node_to_copy[curr].neighbors.append(node_to_copy[nei])
        return node_to_copy[node]