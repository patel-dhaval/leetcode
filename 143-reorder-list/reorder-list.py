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

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr2 = slow.next
        slow.next = None
        prev = None
        temp = None

        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp

        head1 = head
        head2 = prev

        while head1 and head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2

        return head



        