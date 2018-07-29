"""Softmax algorithm."""

from greedy import Greedy
from numpy.random import rand
import random
import numpy as np


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

        if 0 in trials:  # 最初全てのアームを一回ずつ選択する
            return trials.index(0)
        else:
            mus = [self.hits[i] / trials[i] for i in range(self.K)]
            scores = self._softmax(mus)
            return self._sampling_from_pdf(scores)

    def _softmax(self, mus):
        """Softmax function.

        :param mus: list of mu(float)
        :return scores: list of float
        """
        denom = sum([np.exp(mus[i] / self.temp) for i in range(self.K)])
        return [np.exp(mus[i] / self.temp) / denom for i in range(self.K)]

    def _sampling_from_pdf(self, probabilities):
        """Sample from probabilistic distribution function.

        :param probabilities:list of probability(sum of them equals to 1)
        :return arm_num:sampled arm_num from pdf
        """
        probabilities = [sum(probabilities[:x + 1])
                         for x in range(len(probabilities))]
        rand = random.random()
        for arm_num, probability in enumerate(probabilities):
            if rand < probability:
                return arm_num
        return None

    def __str__(self):
        """Override str method."""
        return "<Softmax> N={} Arms={} temp={}".format(self.N, self.arms, self.temp)

    def __repr__(self):
        """Override repr method."""
        return "Softmax({},{},{})".format(self.temp, self.arms, self.N)
