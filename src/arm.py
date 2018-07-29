"""BernoulliArm class."""

from numpy.random import rand


class BernoulliArm():
    """Arm whose distiribution is Bernoulli's one."""

    def __init__(self, mu):
        """Initialize of arm.

        :param mu: (float) the parameter of Bernoulli distiribution
        :return
        """
        self.mu = mu
        return

    def draw(self):
        """Draw from arm.

        :return Bernoulli's r.v
        """
        if rand() <= self.mu:
            return 1
        else:
            return 0

    def __str__(self):
        """Override __str__  method."""
        return "<BernoulliArm> mu: {}".format(self.mu)

    def __repr__(self):
        """Override __repr__  method."""
        return "BernoulliArm({})".format(self.mu)
