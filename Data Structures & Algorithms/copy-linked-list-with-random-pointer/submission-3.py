"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        NodeMap = {None:None}
        curr = head
        while curr:
            NodeMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_node = NodeMap[curr]
            new_node.next = NodeMap[curr.next]
            new_node.random = NodeMap[curr.random]
            curr = curr.next
        return NodeMap[head]
        