'''
Approach

1. Find the middle of the list as the plan would be to reverse the second half of the LL and merge the two halves
2. Use Fast and Slow pointers to find the middle of the list, be careful for both even and odd length of LL
3. Once the middle of the LL is found, we save the starting node for the second half of the LL
4. Reverse the second half of the LL
5. We iterate by moving from the head to the next pointer being the head node of the second half of the LL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head1 = head
        head2 = prev

        while head2:
            temp = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp
            head1 = temp
            head2 = temp2
