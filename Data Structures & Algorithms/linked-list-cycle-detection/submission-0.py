# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        newMap = set()
        curr = head
        while curr:
            if curr not in newMap:
                newMap.add(curr)
                curr = curr.next
            else:
                return True
        return False


        

        
        