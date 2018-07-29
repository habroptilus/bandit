"""UCB algorithm."""

from greedy import Greedy
from numpy.random import rand
import random


class UCB(Greedy):
    """UCB algorithm."""

    def __init__(self, arms, N):
        """Initialization.

        :param arms: list of Arm
        :param n: (int) the number of execution
        :return
        """
        super().__init__(arms, N)
        self.t = 0

    def select_arm(self):
        """Select arm with UCB algorthm."""
        trials = [self.trials[i] for i in range(self.K)]

        if 0 in trials:  # 最初全てのアームを一回ずつ選択する
            self.t += 1
            return trials.index(0)
        else:
            ucbs = [self.hits[i] / trials[i] + math.sqrt(2 * math.log(self.t) / self.trials[i]) + for i in range(self.K)]
            return ucb.index(max(ucbs))

    def __str__(self):
        """Override str method."""
        return "<UCB> N={} Arms={}".format(self.N, self.arms)

    def __repr__(self):
        """Override repr method."""
        return "UCB({},{})".format(self.arms, self.N)
