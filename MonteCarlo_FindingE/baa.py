import random
import time
from numba import jit


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:

    def __init__(self):
        self.n = 0
        self.i = 0

    def throw_points(self, nn):
        (self.i, self.n) = self.throw_points_static(nn)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def throw_points_static(nn):
        i = 0
        for _ in range(nn):
            a = 0
            s = 0
            while s < 1:
                s += random.random()
                a += 1
            i += a
        return i, nn

    def value_of_e(self):
        return self.i / self.n


