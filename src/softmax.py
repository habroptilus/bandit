"""Softmax algorithm."""

from greedy import Greedy
from numpy.random import rand
import random


class Softmax(Greedy):
    """Softmax algorithm."""

    def __init__(self, temp, arms, N):
        """Initialization.

        :param temp: temperature(float)
        :param arms: list of Arm
        :param n: (int) the number of execution
        :return
        """
        super().__init__(arms, N)
        self.temp = temp

    def select_arm(self):
        """Select arm with Softmax algorthm."""
        trials = [self.trials[i] for i in range(self.K)]

    def __str__(self):
        """Override str method."""
        return "<Softmax> N={} Arms={} temp={}".format(self.N, self.arms, self.temp)

    def __repr__(self):
        """Override repr method."""
        return "Softmax({},{},{})".format(self.temp, self.arms, self.N)
