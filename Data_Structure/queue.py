import heapq


class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("QUEUE is Empty!")

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("QUEUE is Empty!")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("QUEUE is Empty!")

    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self.queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0!r})".format(self.name)

    def test_priority_queue():
        # Push와 pop --> (logN)
        q = PriorityQueue()
        q.push(Item('test1'), 1)
        q.push(Item('test2'), 4)
        q.push(Item('test3'), 3)
        assert(str(q.pop()) == "Item('test2')")
        print('Passed the Test')

    if __name__ == "__main__":
        test_priority_queue()
