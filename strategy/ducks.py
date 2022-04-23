"""Ducks implementations."""

from strategy import Duck
from strategy.fly_behaviors import (
    FlyWithWings,
    FlyNoWay,
)
from strategy.quack_behaviors import (
    Quack,
    Squeak,
)


class MallardDuck(Duck):
    """Mallard Duck implementation."""

    def __init__(self):
        """Initialize Mallard Duck."""
        super().__init__(fly_behavior=FlyWithWings(), quack_behavior=Quack())

    @staticmethod
    def display():
        """Display Mallard Duck."""
        print('I am a Mallard Duck')


class RubberDuck(Duck):
    """Rubber Duck implementation."""

    def __init__(self):
        """Initialize Rubber Duck."""
        super().__init__(fly_behavior=FlyNoWay(), quack_behavior=Squeak())

    @staticmethod
    def display():
        """Display Rubber Duck."""
        print('I am a Rubber Duck')


if __name__ == '__main__':

    mallard = MallardDuck()
    mallard.display()
    mallard.fly()
    mallard.quack()

    rubber = RubberDuck()
    rubber.display()
    rubber.fly()
    rubber.quack()
