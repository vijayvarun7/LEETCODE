class MinStack:

    def __init__(self):
        self.items=[]
        self.min=[]

    def push(self, value: int) -> None:
        self.items.append(value)
        if len(self.min)==0:
            self.min.append(value)
        elif self.min[-1]<value:
            self.min.append(self.min[-1])
        else:
            self.min.append(value)

    def pop(self) -> None:
        self.items.pop()
        self.min.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()