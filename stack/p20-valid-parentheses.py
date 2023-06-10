class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Set up a stack and a Hashmap to store valid parentheses
        stack = []
        parenthesesDict = {')': '(', ']':'[', '}':'{'}

        for char in s:
            # Closing Parenthesis
            if char in parenthesesDict:
                if stack and stack[-1] == parenthesesDict[char]:
                    # We were able to successfully match the opening parenthesis in the stack. Take the parenthesis out of the stack
                    stack.pop()
                else:
                    # We expect an opening parenthesis (of the appropriate type) in the stack
                    return False
            else:
                # Add opening parenthesis to stack
                stack.append(char)
        # Check that the stack is empty (all parentheses matched)
        return not stack