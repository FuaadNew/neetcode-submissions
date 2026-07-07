class Solution:
    def calculate(self, s: str) -> int:
        

        op = "+"
        stack = []
        curr = 0

        for i,char in enumerate(s):
            if char.isdigit():
                curr = (curr * 10) + int(char)
            if char in "+-*/" or i == len(s)-1:
                if op == "+":
                    stack.append(curr)
                elif op == "-":
                    stack.append(-curr)
                elif op == "*":
                    stack.append(stack.pop() * curr)
                elif op == "/":
                    stack.append(int(stack.pop() / curr))
                op = char
                curr = 0
            
          
        
        return sum(stack)
                
            



