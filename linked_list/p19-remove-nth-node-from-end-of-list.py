# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head

        # Move right pointer n nodes
        while n > 0:
            right = right.next
            n -= 1
        
        # Move right pointer to end of list while also move left pointer
        while right:
            left = left.next
            right = right.next

        # Remove nth node from the end of the list
        left.next = left.next.next

        # Return the head of the list
        return dummy.next