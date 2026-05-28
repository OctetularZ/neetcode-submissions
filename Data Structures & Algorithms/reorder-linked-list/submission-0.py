# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        curr = head
        rev = prev
        
        while rev:
            next1, next2 = curr.next, rev.next
            curr.next = rev
            rev.next = next1
            curr, rev = next1, next2


        