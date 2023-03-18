class MyQueue:

    def __init__(self):
        self.input_stack = []  # Stack to add elements
        self.output_stack = []  # Stack to remove elements

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self.peek()  # Move elements from input to output stack if output stack is empty
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack
