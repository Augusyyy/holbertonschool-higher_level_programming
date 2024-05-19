#!/usr/bin/python3
"""
This is the SwimMixin module.
This module supplies Mixin
"""


class SwimMixin:
    def swim(self):
        """
        Print a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """
        Print a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """
        Print a message indicating that the dragon roars.
        """
        print("The dragon roars!")
