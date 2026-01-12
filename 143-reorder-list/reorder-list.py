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
        curr = head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr2 = slow.next
        slow.next = None
        prev = None 
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        
        head2 = head
        head3 = prev

        while head2 and head3:
            temp2 = head2.next
            temp3 = head3.next
            head2.next = head3
            head3.next = temp2
            head2 = temp2
            head3 = temp3
        
        return head