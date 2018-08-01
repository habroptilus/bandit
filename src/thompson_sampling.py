"""Thompson Sampling algorithm."""

from bandit import Bandit_algorithm
from numpy.random import rand, beta
import random


class Thompson_sampling(Bandit_algorithm):
    """Thompson Sampling algorithm."""

    def select_arm(self):
        """Select arm with Thompson Sampling algorthm."""
        beta_randoms = [beta(self.hits[i] + 1, self.trials[i] -
                             self.hits[i] + 1) for i in range(self.K)]
        m = max(beta_randoms)
        return beta_randoms.index(m)

    def __str__(self):
        """Override str method."""
        return "<Thompson Sampling> N={} Arms={}".format(self.N, self.arms)

    def __repr__(self):
        """Override repr method."""
        return "Thompson_sampling({},{})".format(self.arms, self.N)
