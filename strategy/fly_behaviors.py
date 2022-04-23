"""FlyBehaviour classes implementations"""

from strategy import FlyBehavior


class FlyWithWings(FlyBehavior):
    """FlyWithWings class"""

    def fly(self):
        """Fly with wings"""
        print("I'm flying with wings!")


class FlyNoWay(FlyBehavior):
    """FlyNoWay class"""

    def fly(self):
        """Fly no way"""
        print("I cant fly!")
