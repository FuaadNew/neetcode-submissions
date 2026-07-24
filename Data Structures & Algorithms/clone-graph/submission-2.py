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
        orig_to_copy = {node: Node(node.val)}
        stack = deque([node])

        while stack:
            curr = stack.popleft()
            if not curr:
                continue

            for nei in curr.neighbors:
                if nei not in orig_to_copy:
                    orig_to_copy[nei] = Node(nei.val)
                    stack.append(nei)
                orig_to_copy[curr].neighbors.append(orig_to_copy[nei])
              

        return orig_to_copy[node]