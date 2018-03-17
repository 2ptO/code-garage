# Implement a queue with 2 stacks. Your queue should have an enqueue and a 
# dequeue method and it should be "first in first out" (FIFO).
# Q17, Q18 were javascript questions. 

DEFAULT_STACK_SIZE = 16

class QueueUsingStack:
    """
    Implements a queue using two stacks, with a default size of 16
    """
    def __init__(self, size=DEFAULT_STACK_SIZE):
        self.size = size
        self.in_stack = []
        self.out_stack = []
        self.n_items = 0
    
    def enqueue(self, item):
        # TODO stack overflow
        if self.n_items >= DEFAULT_STACK_SIZE:
            raise OverflowError("Queue is full")

        self.in_stack.append(item)
        self.n_items += 1
    
    def dequeue(self):
        # stack underflow
        if not self.in_stack and not self.out_stack:
            # Python's pop handle the underflow error. Making an explicit
            # check for just correctness
            raise IndexError("can't pop from empty list")
        
        # If out stack is empty, move items from in_stack to out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        self.n_items -= 1
        return self.out_stack.pop()

# Complexity analysis was little tricky in this case.
# Say we enqueue and dequeue 'n' items, time cost can
# be derived as O(n) if both enqueue and dequeue runs in O(1) time.
# As seen in the code, enqueue() runs in O(1) time. 
# For dequeue, some calls in O(1) and some run in O(n) time.
# Another way to look at this is, each item in the stack goes
# through a constant of 4 operations:
# 1. push into in_stack
# 2. pop from in_stack
# 3. push into out_stack
# 4. pop from out_stack
# Since per item cost is constant, we can amortize this as O(1) for
# dequeue() operation too. Hence the overall time cost O(n)
# Space cost is O(2n) -> O(n).
