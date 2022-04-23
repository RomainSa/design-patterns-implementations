"""QuackBehaviour classes implementations"""

from strategy import QuackBehavior


class Quack(QuackBehavior):
    """Quack class"""

    def quack(self):
        """Common quack"""
        print("Quack quack")


class Squeak(QuackBehavior):
    """Squeak class"""

    def quack(self):
        """Rubber duck quack"""
        print("Squeak squeak")


class Mute(QuackBehavior):
    """Mute class"""

    def quack(self):
        """Mute quack"""
        pass
