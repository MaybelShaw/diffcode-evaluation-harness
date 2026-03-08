import math
from .base import Metric


class PassK(Metric):
    def __init__(self, k):
        self.k = k

    def evaluate(self, results):
        n = len(results)
        c = sum(results)

        if n - c < self.k:
            return 1.0

        return 1 - math.comb(n - c, self.k) / math.comb(n, self.k)
