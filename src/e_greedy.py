"""Epsilon Greedy algorithm."""

from bandit import Bandit_algorithm
from numpy.random import rand
import random


class Epsilon_greedy(Bandit_algorithm):
    """Epsilon Greedy algorithm."""

    def __init__(self, epsilon, arms, N):
        """Initialization.

        :param epsilon: threshold(float)
        :param arms: list of Arm
        :param n: (int) the number of execution
        :return
        """
        super().__init__(arms, N)
        self.e = epsilon

    def select_arm(self):
        """Select arm with e_greedy algorthm."""
        trials = [self.trials[i] for i in range(self.K)]

        if 0 in trials:  # 最初全てのアームを一回ずつ選択する
            return trials.index(0)
        else:
            if rand() < self.e:
                return random.choice(list(range(self.K)))
            else:
                prob = [self.hits[i] / trials[i] for i in range(self.K)]
                return prob.index(max(prob))

    def __str__(self):
        """Override str method."""
        return "<e-Greedy> N={} Arms={} e={}".format(self.N, self.arms, self.e)

    def __repr__(self):
        """Override repr method."""
        return "Epsilon_greedy({},{},{})".format(self.e, self.arms, self.N)
