#!/usr/bin/python3
"""
This is the Fish module.
This module supplies mul inheritance
"""


class Fish:
    def swim(self):
        """
        Print a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    def fly(self):
        """
        Print a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """
        Print a message indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print a message indicating the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
