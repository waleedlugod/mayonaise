#!/usr/bin/env python3


class RingBuffer:
    def __init__(self, capacity: int):
        """
        Create an empty ring buffer, with given max capacity
        """
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = -1
        self._rear = -1
        self.buffer = [None] * capacity
        self.bufferSize = 0

    def size(self) -> int:
        """
        Return number of items currently in the buffer
        """
        return self.bufferSize
        """
        if self._rear > self._front:
            return (self._rear-self._front+1)
        elif self._rear < self._front:		# the rear is past the capacity
            return (self.MAX_CAP-self._front+1) + (self._rear+1)
        else:
            return(0)
        """

    def is_empty(self) -> bool:
        """
        Is the buffer empty (size equals zero)?
        """
        # TO-DO: implement this
        return self.size() == 0

    def is_full(self) -> bool:
        """
        Is the buffer full (size equals capacity)?
        """
        # TO-DO: implement this
        return self.size() == self.MAX_CAP

    def enqueue(self, x: float):
        """
        Add item `x` to the end
        """
        # TO-DO: implement this
        if self.size() == self.MAX_CAP:
            raise RingBufferFull
        elif self._front == -1:
            self._front += 1
            self._rear += 1
        elif self._rear == self.MAX_CAP - 1:
            self._rear = 0
        else:
            self._rear += 1

        self.buffer[self._rear] = x
        self.bufferSize += 1

    def dequeue(self) -> float:
        """
        Return and remove item from the front
        """

        # TO-DO: implement this

        if self.size() == 0:
            raise RingBufferEmpty

        to_remove = self.buffer[self._front]
        self.buffer[self._front] = None

        if self._front == self.MAX_CAP - 1:
            self._front = 0
        else:
            self._front += 1

        self.bufferSize -= 1

        return to_remove

    def peek(self) -> float:
        """
        Return (but do not delete) item from the front
        """
        # TO-DO: implement this
        if self.size() == 0:
            raise RingBufferEmpty
        else:
            return self.buffer[self._front]


class RingBufferFull(Exception):
    pass


class RingBufferEmpty(Exception):
    pass
