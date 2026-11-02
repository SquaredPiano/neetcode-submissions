class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+/-*":
                stack.append(int(token))
            else:
                operand_two = stack.pop()
                operand_one = stack.pop()
                if token == "+":
                    stack.append(operand_one + operand_two)
                elif token == "-":
                    stack.append(operand_one - operand_two)
                elif token == "/":
                    stack.append(int(operand_one / operand_two))
                elif token == "*":
                    stack.append(operand_one * operand_two)
        
        return stack[0]