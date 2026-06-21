# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #split list in two
        second = slow.next
        slow.next = None
        First = head


        #reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
        


        