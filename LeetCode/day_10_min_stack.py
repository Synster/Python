"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""


class MinStack:
    """
    keep two stacks 1 nubers another min stack
    while pushing push to both if x<top min_stack push x on min_stack else push top of min stack again on it
    pop from both stack to keep them in sync
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, x: int) -> None:
        if self.is_empty():
            self.stack.append(x)
            self.min.append(x)
        else:
            self.stack.append(x)
            y = self.min.pop()
            self.min.append(y)
            if x < y:
                self.min.append(x)
            else:
                self.min.append(y)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        x = self.stack.pop()
        self.stack.append(x)
        return x

    def getMin(self) -> int:
        x = self.min.pop()
        self.min.append(x)
        return x


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack)
print(obj.getMin())
obj.pop()
print(obj.stack)
print(obj.top())
print(obj.getMin())
