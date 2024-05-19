#!/usr/bin/python3
"""
This is the VerboseDict module.
This module supplies override
"""


class VerboseDict(dict):
    def __init__(self, *args, **kwargs):
        """
        Initialize the VerboseDict with the given arguments
        and keyword arguments.Also, initialize an empty list
        to keep the history of operations.
        """
        super().__init__(*args, **kwargs)
        self._history = []

    def __setitem__(self, key, value):
        """
        Set the item in the dictionary and record the action
        in the history. If the key already exists, record an
        update action. Otherwise, record an addition action.
        """
        if key in self:
            self._history.append(f"Updated: {key} -> {value}")
        else:
            self._history.append(f"Added: {key} -> {value}")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        """
        Delete the item from the dictionary and record the action
        in the history.Record a removal action.
        """
        self._history.append(f"Removed: {key}")
        super().__delitem__(key)

    def get_history(self):
        """
        Return the history of all the operations performed on the dictionary.
        """
        return self._history
