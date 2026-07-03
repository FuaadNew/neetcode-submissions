# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(l):
            prev = None
            curr = l

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        
        curr = None
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            val = l1_val + l2_val + carry
            carry = val // 10
            val = val % 10
            valNode = ListNode(val)
            valNode.next = curr
            curr = valNode
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return curr






        



