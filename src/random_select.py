"""Random algorithm."""

from bandit import Bandit_algorithm
from numpy.random import rand
import random
import numpy as np


class Random_select(Bandit_algorithm):
    """Random algorithm."""

    def __init__(self, temp, arms, N):
        """Initialization.

        :param temp: temperature(float)
        :param arms: list of Arm
        :param n: (int) the number of execution
        :return
        """
        super().__init__(arms, N)

    def select_arm(self):
        """Select arm with Random select algorthm."""
        return random.choice(list(range(self.K)))

    def __str__(self):
        """Override str method."""
        return "<Random> N={} Arms={}".format(self.N, self.arms)

    def __repr__(self):
        """Override repr method."""
        return "Random_select({},{})".format(self.arms, self.N)
