# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        curr_sum = 0 
        curr_carr = 0
        dummy = ListNode(0, None)
        head = dummy
        while l1 or l2 or curr_carr:
            curr_sum = curr_carr 
            if l1:
                curr_sum += (l1.val)
                l1 = l1.next
            if l2:
                curr_sum += (l2.val)
                l2 = l2.next
            curr_carr = curr_sum//10

            sum_node = ListNode((curr_sum%10), None)
            dummy.next = sum_node
            dummy = dummy.next

        return head.next