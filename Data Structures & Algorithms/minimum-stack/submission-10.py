class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        else:
            new_min = min(self.min[-1], val)
            self.min.append(new_min)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
