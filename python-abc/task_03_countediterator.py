#!/usr/bin/python3
"""
This is the CountedIterator module.
This module supplies iter() next()
"""


class CountedIterator:
    """
    A class to wrap around an iterable and count the number
    of items iterated over.

    Attributes:
    -----------
    iterator : iterator
        The iterator object created from the provided iterable.
    count : int
        A counter to track the number of items iterated over.

    Methods:
    --------
    get_count():
        Returns the current value of the counter.
    __next__():
        Returns the next item from the iterator and increments the counter.
    __iter__():
        Returns the iterator object itself.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Parameters:
        -----------
        iterable : iterable
            The iterable to be wrapped by the CountedIterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current count of iterated items.

        Returns:
        --------
        int
            The current value of the counter.
        """
        return self.count

    def __next__(self):
        """
        Returns the next item from the iterator and increments the counter.

        Raises:
        -------
        StopIteration
            If there are no items left to iterate over.

        Returns:
        --------
        any
            The next item from the iterator.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
        --------
        CountedIterator
            The iterator object.
        """
        return self
