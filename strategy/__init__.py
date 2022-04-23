"""
Strategy pattern implementation

Contains the Duck abstract class
"""

from abc import (
    ABC,
    abstractmethod,
)


class FlyBehavior(ABC):
    """Fly behavior abstract class"""

    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(ABC):
    """Quack behavior abstract class"""

    @abstractmethod
    def quack(self):
        pass


class Duck(ABC):
    """Duck abstract class"""

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()
