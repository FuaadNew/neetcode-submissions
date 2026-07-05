# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        
        carry = 0
        while stack1 or stack2 or carry:
            l1,l2 = None, None
            if stack1:
                l1 = stack1.pop()
            if stack2:
                l2 = stack2.pop()
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            val = l1_val + l2_val + carry
            print(val)
            carry = val//10
            val = val % 10
            new_node = ListNode(val)
            new_node.next = curr
            curr = new_node
        return curr

            

