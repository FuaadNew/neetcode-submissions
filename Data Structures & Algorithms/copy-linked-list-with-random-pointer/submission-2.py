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
        Nodemap = {None:None}
        curr = head
        while curr:
            Nodemap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_node = Nodemap[curr]
            new_node.next = Nodemap[curr.next]
            new_node.random = Nodemap[curr.random]
            curr = curr.next 
        return Nodemap[head]
            

        