# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l2

        dummy = ListNode()
        curr = dummy
        carry = None

        while l1 and l2:
            if carry:
                total = l1.val + l2.val + carry
            else:
                total = l1.val + l2.val

            if total >= 10:
                curr.next = ListNode(total % 10)
                carry = total // 10
            else:
                curr.next = ListNode(total)
                carry = None

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        left_over = l1 or l2

        while left_over:
            if carry:
                total = left_over.val + carry
            else:
                total = left_over.val
            
            if total >= 10:
                curr.next = ListNode(total % 10)
                carry = total // 10
            else:
                curr.next = ListNode(total)
                carry = None
            
            curr = curr.next
            left_over = left_over.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
    

# Use two pointers, one for each list
# At each iteration, add both numbers
# If number, below respective place value, add to new linked list and continue
# Else: if above respective place value, divide by respective place value and add remiander to linked list
# Can just divide by 10 each time I believe as it's relative as long as I don't increase numbers by actual place value and leave as single digits.
# Then carry over the amount to next addition
# If no carry, set carry to None to we can check at end.
# Repeat until the end is reached. Add remaining carry over to end.
