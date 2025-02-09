# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
A technique is used for cycle detection in Linkedlists which is known as slow and fast pointers
We use 2 pointer, both pointing to head initially, but we move the slow pointer by 1 and fast pointer by 2
We loop till slow pointer reached the end of the list
If there is a case that the slow and fast pointers intersect, then we can be sure that there exists a cycle in the List

"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False