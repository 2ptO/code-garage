# Use a Stack class to implement a new class MaxStack with a method get_max()
# that returns the largest element in the stack. get_max() should not remove the item.

class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, new_element):
        """
        Pushes the new_element to the top of the stack
        """
        self.elements.append(new_element)
    
    def pop(self):
        """
        Pops the top element from the stack and returns it.
        Returns None if stack is empty
        """
        if self.elements:
            return self.elements.pop()
        else:
            return None
    
    def peek(self):
        if self.elements:
            return self.elements[-1]
        else:
            return None

class MaxStack:
    def __init__(self):
        self.stack = Stack()

        # if we track the new max as we insert new items,
        # we will lose the max_element if the max_element
        # is popped from the stack. And, we will have to
        # to another series of push/pop to find the next
        # max_element in the stack. So, we need a way to
        # keep track of second max_element. With Stack, since
        # we pop items in last-in-first-out order, each
        # time we find a new max, the new_max holds good
        # for the elements that were in the stack at that time.
        # e.g. inputs = [10, 9, 4, 15, 14, 20, 2]
        # stack: [10]                      max_element: 10
        # stack: [10 9]                    max_element: 10
        # stack: [10 9 4]                  max_element: 10
        # stack: [10 9 4 15]               max_element: 15
        # stack: [10 9 4 15 14]            max_element: 15
        # stack: [10 9 4 15 14 20]         max_element: 20
        # stack: [10 9 4 15 14 20 2]       max_element: 20
        # If we pop 2, max_element is going to change. If we
        # pop 20, the next max_element is 15. If we maintain
        # parallel stack to keep track of max elements,
        # we can return the max_element in O(1)

        self.max_stack = Stack()
    
    def push(self, new_element):
        current_max = self.max_stack.peek()
        if current_max is None or new_element > current_max:
                self.max_stack.push(new_element)
        self.stack.push(new_element)

    def pop(self):
        popped_element = self.stack.pop()
        # If popped_element is the current max, pop it from
        # the max_stack as well
        if popped_element == self.max_stack.peek():
            self.max_stack.pop()
        return popped_element
    
    def get_max(self):
        return self.max_stack.peek()

