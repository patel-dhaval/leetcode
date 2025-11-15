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

            if slow == fast:
                break

        prev = None
        head2 = slow.next
        slow.next = None

        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        head3 = head
        head4 = prev


        while head3 and head4:
            # print(head3.val, head4.val)
            temp1, temp2 = head3.next, head4.next
            head3.next = head4
            head4.next = temp1
            head3 = temp1
            head4 = temp2
        
        return head