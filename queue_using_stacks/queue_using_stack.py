'''
The module defines a queue using 2 stacks
'''
class Node:
    '''
    Defines nodes
    '''
    def __init__(self, data):
        '''
        Receives value of data
        '''
        self.data = data
        self.next = None

class Stack:
    '''
    Defines a stack
    '''
    def __init__(self):
        self.top = None

    def push(self, data):
        '''
        Pushes the value to the stack
        '''
        st_data = Node(data)
        if self.top is None:
            self.top = st_data
        else:
            st_data.next = self.top
            self.top = st_data


    def pop(self):
        '''
        Pops the value from the stack
        '''
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        '''
        Peeks the value of the stack
        '''
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        '''
        Cheks, whether the stack is empty
        '''
        return self.top is None


class MyQueue:
    '''
    Defines a queue using 2 stacks
    '''
    def __init__(self):
        '''
        Initialize 2 stacks
        '''
        self.st1 = Stack()
        self.st2 = Stack()

    def push(self, x: int) -> None:
        '''Pushes the value to the queue'''
        self.st1.push(x)

    def pop(self) -> int:
        '''Pops the value to the queue'''
        if self.st2.is_empty():
            while not self.st1.is_empty():
                self.st2.push(self.st1.pop())
        return self.st2.pop()


    def peek(self) -> int:
        '''Peeks the value to the queue'''
        if self.st2.is_empty():
            while not self.st1.is_empty():
                self.st2.push(self.st1.pop())
        return self.st2.peek()

    def empty(self) -> bool:
        '''Checks, whether the queue is empty'''
        return self.st1.is_empty() and self.st2.is_empty()
