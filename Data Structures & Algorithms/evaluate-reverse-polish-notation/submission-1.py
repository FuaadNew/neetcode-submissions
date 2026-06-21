class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notationList = ['+','-','*','/']
        stack = []
        res = 0
        for string in tokens:
            if string not in notationList:
                stack.append(string)
            elif string == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 + num2)
            elif string == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif string == "*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 * num2)
            elif string == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(int(num1 / num2))
            
        return int(stack[-1])
         