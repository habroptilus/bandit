"""Greedy algorithm."""
import pandas as pd


class Greedy():
    """Greedy algorithm."""

    def __init__(self, arms, N):
        """Initialization.

        :param arms: list of Arm
        :param n: (int) the number of execution
        :return
        """
        self.arms = arms
        self.N = N
        self.K = len(arms)  # the number of arms
        self.trials = [0] * self.K
        self.hits = [0] * self.K

    def select_arm(self):
        """Select arm with greedy algorthm."""
        trials = [self.trials[i] for i in range(self.K)]
        if 0 in trials:  # 最初全てのアームを一回ずつ選択する
            return trials.index(0)
        else:
            prob = [self.hits[i] / trials[i] for i in range(self.K)]
            return prob.index(max(prob))

    def execute(self):
        """Execute this algorithm.

        :return df: DataFrame containing arm and reward columns.
        """
        df = pd.DataFrame()
        for i in range(self.N):
            row = pd.DataFrame()
            arm_num = self.select_arm()
            reward = self.arms[arm_num].draw()
            self.trials[arm_num] += 1
            if reward == 1:
                self.hits[arm_num] += 1
            row["arm"] = [arm_num]
            row["reward"] = [reward]
            df = pd.concat([df, row], ignore_index=True)
        return df

    def __str__(self):
        """Override str method."""
        return "<Greedy> N={} Arms={}".format(self.N, self.arms)

    def __repr__(self):
        """Override repr method."""
        return "Greedy({},{})".format(self.arms, self.N)
