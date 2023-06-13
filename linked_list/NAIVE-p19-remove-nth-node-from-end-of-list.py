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

        # Determine then size of the linked list
        temp = head
        size = 0
        while head.next != None:
            size += 1
            head = head.next

        # Go to the node to remove
        prev = None
        head = temp
        for i in range(size-n+1):
            prev = head
            head = head.next
        
        # Remove the nth node from the end of the list
        if prev:
            prev.next = head.next
        
        else:
            # Case where there is no previous node (eg. first node in linked list)
            temp = head.next

        return temp
