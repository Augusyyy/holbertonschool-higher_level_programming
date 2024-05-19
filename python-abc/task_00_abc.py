#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This is the Animal module.
This module supplies abstractmethod
"""


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
