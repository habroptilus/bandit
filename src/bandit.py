"""Bandit algorithm."""
import pandas as pd


class Bandit_algorithm():
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
        """Select arm."""
        pass

    def execute(self):
        """Execute this algorithm.

        :return df: DataFrame containing arm and reward columns.
        """
        df = pd.DataFrame()
        arm_num_list = []
        reward_list = []
        for i in range(self.N):
            arm_num = self.select_arm()
            reward = self.arms[arm_num].draw()
            self.trials[arm_num] += 1
            if reward == 1:
                self.hits[arm_num] += 1
            arm_num_list.append(arm_num)
            reward_list.append(reward)
        df["arm"] = arm_num_list
        df["reward"] = reward_list
        return df
