class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*',  '/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    last_val = stack.pop()
                    stack[-1]+= last_val
                elif token == "-":
                    last_val = stack.pop()
                    stack[-1]-= last_val
                elif token == "*":
                    last_val = stack.pop()
                    stack[-1]*= last_val
                elif token == "/":
                    last_val = stack.pop()
                    stack[-1] = int(stack[-1] / last_val)
        return stack[-1]
                


