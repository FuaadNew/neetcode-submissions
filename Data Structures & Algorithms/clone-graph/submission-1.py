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
        graph_dict = {}

        #go through every node and map the original node to it's copy

        def dfs(orig):
            if not orig:
                return
            clone = Node(orig.val)
            graph_dict[orig] = clone
            for nei in orig.neighbors:
                if nei in graph_dict:
                    clone.neighbors.append(graph_dict[nei])
                else:
                    clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)
