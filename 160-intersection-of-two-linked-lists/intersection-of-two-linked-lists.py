# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = 0
        len_b = 0
        curr_a = headA
        curr_b = headB

        def compareNodes(curr_a, curr_b):
            if curr_a == curr_b:
                return True
            return False

        
        while curr_a:
            len_a += 1
            curr_a = curr_a.next
        
        
        while curr_b:
            len_b += 1
            curr_b = curr_b.next

        curr_a = headA
        curr_b = headB
        
        if len_a > len_b:
            while len_a > len_b:
                if compareNodes(curr_a, curr_b):
                    return curr_a
                len_a -= 1
                curr_a = curr_a.next

        elif len_a < len_b:
            while len_a < len_b:
                if compareNodes(curr_a, curr_b):
                    return curr_b
                len_b -= 1
                curr_b = curr_b.next

        while curr_a and curr_b:
            if compareNodes(curr_a, curr_b):
                return curr_a
            curr_a = curr_a.next
            curr_b = curr_b.next
        
        return None


        
        
        
