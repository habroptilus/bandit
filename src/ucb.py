"""UCB algorithm."""

from bandit import Bandit_algorithm
from numpy.random import rand
import random
import math


class UCB(Bandit_algorithm):
    """UCB algorithm."""

    def __init__(self, arms, N):
        """Initialization.

        :param arms: list of Arm
        :param n: (int) the number of execution
        :return
        """
        super().__init__(arms, N)

    def select_arm(self):
        """Select arm with UCB algorthm."""
        trials = [self.trials[i] for i in range(self.K)]
        t = sum(self.trials)
        if 0 in trials:  # 最初全てのアームを一回ずつ選択する
            return trials.index(0)
        else:
            ucbs = [self.hits[i] / trials[i] +
                    math.sqrt(math.log(t) / (2 * self.trials[i])) for i in range(self.K)]
            return ucbs.index(max(ucbs))

    def __str__(self):
        """Override str method."""
        return "<UCB> N={} Arms={}".format(self.N, self.arms)

    def __repr__(self):
        """Override repr method."""
        return "UCB({},{})".format(self.arms, self.N)
