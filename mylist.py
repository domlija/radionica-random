class Node():
    def __init__(self, next, val):
        self._next = next 
        self._val = val

    def __str__(self):
        return str(self._val)

class LinkedList():
    def __init__(self, iterable=None):
        self._head = None
        self._tail = None

    def append(self, val):
        new_node = Node(None, val)
        if not self._head:
            self._head = new_node
            self._tail = new_node

        else:
            self._tail._next = new_node
            self._tail = new_node

    def get(self, index):
        current = 0
        current_node = self._head

        

        while current != index:
            if current_node == None:
                raise Exception('Index to large')
            current += 1
            current_node = current_node._next

        if current_node == None:
            raise Exception('Index to large')
        
        return current_node._val

    def pop(self, index):
        current = 0
        current_node = self._head

        

        while current < index - 1:
            if current_node == None:
                raise Exception('Index to large')
            current += 1
            current_node = current_node._next

        if current_node == None or current_node._next == None:
            raise Exception('Index to large')
        
        helper_node = current_node._next
        current_node._next = helper_node._next

        
        
        

        
            
    
    def __str__(self):
        return_string = '['
        next_node = self._head

        while next_node:
            return_string += str(next_node._val) + ', '
            next_node = next_node._next
        
        return return_string[ : len(return_string) - 2] + ']'


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l)
l.pop(3)
print(l)
    

