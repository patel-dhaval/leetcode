# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1. Start with a dummy node
2. Compare the values of heads of both lists
3. Whichever is smaller, dummy node points to that one
4. Keep going till we reach the end of either of the two lists
5. Then keep adding the values from the list whichever has any left over values, since the list is sorted, this will work just fine.
6. Return dummy.next to get the merged sorted lists

'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr =  ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return dummy.next