class Solution:
    def calculate(self, s: str) -> int:
        
        op = "+"
        stack = []
        curr = 0
        


        for i,char in enumerate(s):
            if char.isdigit():
                curr = (curr * 10) + int(char)
            if char in "+-/*" or i == len(s)-1:
                if op == "+":
                    stack.append(curr)
                elif op == "-":
                    stack.append(-curr)
                elif op == "*":
                    stack.append(stack.pop() * curr)
                else:
                    stack.append(int(stack.pop() / curr))
                curr = 0
                op = char
            
        return sum(stack)