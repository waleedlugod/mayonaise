#!/usr/bin/env python3
from math import ceil
import random
from ringbuffer import *


class GuitarString:
    def __init__(self, frequency: float):
        """
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        """
        self.ticks = 0
        self.ticks_last_plucked = 0
        self.capacity = ceil(44100 / frequency)
        self.buffer = RingBuffer(self.capacity)
        while not self.buffer.is_full():
            self.buffer.enqueue(0)

    @classmethod
    def make_from_array(cls, init: list[int]):
        """
        Create a guitar string whose size and initial values are given by the array `init`
        """
        # create GuitarString object with placeholder freq
        stg = cls(1000)
        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        """
        Set the buffer to white noise
        """
        for x in range(self.buffer.size()):
            self.buffer.dequeue()
            self.buffer.enqueue(random.uniform(-1 / 2, 1 / 2))
        self.ticks_last_plucked = self.ticks

    def tick(self):
        """
        Advance the simulation one time step by applying the Karplus--Strong update
        """
        self.ticks += +1
        num1 = self.buffer.dequeue()
        num2 = self.buffer.peek()
        self.buffer.enqueue((num1 + num2) * 0.996 / 2)

    def sample(self) -> float:
        """
        Return the current sample
        """
        return self.buffer.peek()

    def time(self) -> int:
        """
        Return the number of ticks so far
        """
        return self.ticks

    def ticks_after_plucked(self) -> int:
        """
        Return the number of ticks since plucked
        """
        return self.time() - self.ticks_last_plucked
