from io import StringIO
import sys

"""_summary_
# Sto je dodano:

- Pravilni prikaz svih datatypeova
- Popravljeni pop, sada radi
- Sliceanje (npr linklista[1])
- Novi test caseoci u mainu
- Errori vise nisu samo Exception, nego vec IndexError 
"""

def PrintfToString(anydata, use_repr_for_printout: bool = True):
    stdout_buffer = StringIO()
    sys.stdout = stdout_buffer
    if use_repr_for_printout: 
        print(repr(anydata), end="") ##
    else:
        print(anydata, end="")
    printf_output = stdout_buffer.getvalue()
    sys.stdout = sys.__stdout__
    return printf_output


class Node():
    def __init__(self, next, val):
        self._next = next 
        self._val = val

    def __str__(self):
        return PrintfToString(self._val)
    

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
                raise IndexError('Index out of range.')
            current += 1
            current_node = current_node._next

        if current_node == None:
            raise IndexError('Index out of range.')
        
        return current_node._val
    
    def __getitem__(self, index):
        return self.get(index=index)

    def pop(self, index):
        current = 0
        current_node = self._head

        

        while current < index - 1:
            if current_node == None:
                raise IndexError('Index out of range.')
            current += 1
            current_node = current_node._next

        if current_node == None or current_node._next == None:
            raise IndexError('Index out of range.')
        
        helper_node = current_node._next
        current_node._next = helper_node._next
        
        ## FIX ZA DOMACI RAD
        
        if current_node._next is None:  # ako ne postoji next (tail)
            self._tail = current_node   # tail mora biti None

    def __str__(self):
        return_string = '['
        next_node = self._head

        is_first = True
        while next_node:
            if is_first:
                return_string += PrintfToString(next_node._val)
                is_first = False
                next_node = next_node._next
                continue
            return_string +=  ', ' + PrintfToString(next_node._val)
            next_node = next_node._next
        
        return return_string + ']' #[ : len(return_string) - 2] + ']'

if __name__ == "__main__":
    print(f"Running as {__name__}, test eval")
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    print(l)
    l.pop(3)
    print(l)
    l.append(5)
    print(l)
    l.append("test")
    print(l)
    l.pop(2)
    print(l)
    print("Nadam se da radi slice", l[2])

