# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0, head)

        # Find middle node of linked list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # Beginning of 2nd half of list
        slow.next = None # Split into 2 linked lists (1st half and 2nd half)

        # Reverse 2nd half of list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge 2 halves of linked list
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            # Insert node in 2nd half in between nodes in the 1st half (eg. 1 -> 2 -> 4 becomes 1 -> 4 -> 2)
            first.next = second
            second.next = temp1
            # Go to next node in both halves
            first, second = temp1, temp2
        
        # Time Complexity: O(n) - note that we iterate through the list twice but this has no impact on the time complexity
        # Space Complexity: O(1)