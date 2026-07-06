class Solution:
    def calculate(self, s: str) -> int:
        
        curr = 0
        stack = []
        op = "+"
        for i,char in enumerate(s):
            if char.isdigit():
                curr = (curr * 10) + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(curr)
                elif op == "-":
                    stack.append(-curr)
                elif op == "*":
                    stack.append(stack.pop() * curr)
                elif op == "/":
                    stack.append(int(stack.pop()/ curr))

                curr = 0
                op = char
        return sum(stack)
