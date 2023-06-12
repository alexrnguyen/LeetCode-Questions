class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for char in tokens:
            if char  in {"+", "-", "*", "/"}:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if char == "+":
                    result = operand1 + operand2
                elif char == "-":
                    result = operand1 - operand2
                elif char == "*":
                    result = operand1 * operand2
                else:
                    result = int(float(operand1) / operand2)
                stack.append(result)
            else:
                stack.append(int(char))
        return stack.pop()