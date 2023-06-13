class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize two pointers at each end of string
        left = 0
        right = len(s) - 1

        # Continue until two pointer cross each other
        while left <= right:
            # Loop until a alpha-numeric character is found (stop if pointers cross)
            while left < right and not s[left].isalnum():
                left = left + 1
            while left < right and not s[right].isalnum():
                right = right - 1
            if s[left].lower() != s[right].lower():
                return False
            left = left + 1
            right = right - 1
        return True