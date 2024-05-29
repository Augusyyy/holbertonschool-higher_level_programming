#!/usr/bin/python3
"""Create a custom Python class named customobject .
This class should have the following attributes:"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Create a custom Python class named customobject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print out the object's attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Student: {}".format(self.is_student))

    def serialize(self, filename):
        """will take a filename as its parameter"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(self, filename):
        """using the pickle module,it wi load and return an instance"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except EOFError:
            return None
