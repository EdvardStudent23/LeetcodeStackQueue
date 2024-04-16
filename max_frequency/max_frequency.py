'''
The module has an implementation
'''
from collections import defaultdict
class Node:
    '''
    Defines a node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''
    Defines a stack
    '''
    def __init__(self):
        '''
        receives a value
        '''
        self.top = None

    def push(self, elem):
        '''
        The function pushes a new element to the stack
        '''
        new_node = Node(elem)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        '''
        Pops an element from the stack
        '''
        if self.is_empty():
            return None
        elem = self.top.data
        self.top = self.top.next
        return elem

    def peek(self):
        '''
        Return a value 
        '''
        if self.top:
            return self.top.data
        return None

    def is_empty(self):
        '''
        Checks whether the stack is empty
        '''
        return self.top is None

class FreqStack:
    '''
    Pops the most frequent element from the stack.
    '''
    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_max = 0
        self.freq_elem = defaultdict(Stack)

    def push(self, val: int) -> None:
        '''
        Push the value to the stack
        '''
        self.freq[val] += 1
        freq = self.freq[val]
        self.freq_max = max(freq, self.freq_max)
        self.freq_elem[freq].push(val)

    def pop(self) -> int:
        '''
        Pops the elemnt from a stack
        '''
        elem = self.freq_elem[self.freq_max].pop()
        self.freq[elem] -= 1
        if self.freq[elem] == 0:
            del self.freq[elem]
        if self.freq_elem[self.freq_max].is_empty():
            self.freq_max -= 1
        return elem
