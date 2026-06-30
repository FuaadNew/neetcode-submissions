class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = [ '+', '-', '*',  '/']
        stack = []
       

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    operand_1 = stack.pop()
                    stack[-1]+= operand_1
                    
                if token == "-":
                    operand_1 = stack.pop()
                    stack[-1]-= operand_1
                    
                if token == "*":
                    operand_1 = stack.pop()
                    stack[-1]*= operand_1

                if token == "/":
                    operand_1 = stack.pop()
                    stack[-1]= int(stack[-1] / operand_1)

        return stack[-1] 


                    
