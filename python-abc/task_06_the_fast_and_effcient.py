#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This is the Vehicle module.
This module supplies abstractmethod
"""


class Vehicle(ABC):
    @abstractmethod
    def fuel_efficiency(self):
        """
        Return the fuel efficiency of the vehicle.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def top_speed(self):
        """
        Return the top speed of the vehicle.
        This method must be implemented by subclasses.
        """
        pass


class Car(Vehicle):
    def __init__(self, make, model, year):
        """
        Initialize the car with make, model, and year.
        """
        self.make = make
        self.model = model
        self.year = year

    def fuel_efficiency(self):
        """
        Return the fuel efficiency of the car.
        """
        return "30 miles per gallon"

    def top_speed(self):
        """
        Return the top speed of the car.
        """
        return "150 mph"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        """
        Initialize the motorcycle with make, model, and year.
        """
        self.make = make
        self.model = model
        self.year = year

    def fuel_efficiency(self):
        """
        Return the fuel efficiency of the motorcycle.
        """
        return "50 miles per gallon"

    def top_speed(self):
        """
        Return the top speed of the motorcycle.
        """
        return "120 mph"
