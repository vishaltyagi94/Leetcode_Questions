class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.lastIdx = -1
        self.minElem = []
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.minElem.append(x)
        elif x <= self.minElem[-1]:
            self.minElem.append(x)
        self.stack.append(x)
        

    def pop(self) -> None:
        if self.stack[-1] == self.minElem[-1]:
            self.minElem.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minElem[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
