class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        if len(self.stack)==0 :
            self.stack.append(val)
            self.minstack.append(val)
            return
        min=val if self.minstack[-1]>val else self.minstack[-1] 
        self.stack.append(val)
        self.minstack.append(min)
        
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()