'''
This modul allows to make a stack using 2 queque
'''
class Node:
    '''
    Defines a class for a node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    '''
    Defines a queue 
    '''
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        '''
        Make enqueque
        '''
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        '''
        Make dequeque
        '''
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        '''
        Defines a peek function 
        '''
        if self.is_empty():
            return None
        return self.front.data

    def is_empty(self):
        '''
        Checks whether the queque is empty
        '''
        return self.front is None

class MyStack:
    '''
    Class defines a stack
    '''
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        '''
        Function for pushing the info 
        '''
        self.queue2.enqueue(x)
        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        '''
        Pop the element from a stack
        '''
        return self.queue1.dequeue()

    def top(self) -> int:
        '''
        Returns the top element
        '''
        return self.queue1.peek()

    def empty(self) -> bool:
        '''
        Checks, whether the stack is empty
        '''
        return self.queue1.is_empty()
