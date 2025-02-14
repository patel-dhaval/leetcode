'''
Approach

The solution of this would be a slightly modified version of slow and fast pointers
We will take two pointers, and move them n places apart, n will be part of the input given
Once the nodes are n-spaces apart, we move the nodes by 1 spaces till the second node reaches the end of the list
Once the second node reaches the end, we will have the first node at n-1th spot from the end of the list
We simply update the pointers and we drop the nth node
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None

        dummy = ListNode(0, head)
        first = dummy
        second = head

        while n > 0:
            second = second.next
            n = n-1
        
        while second:
            first = first.next
            second = second.next

        
        first.next = first.next.next

        return dummy.next
