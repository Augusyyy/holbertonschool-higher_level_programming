#!/usr/bin/python3
"""
This is the VerboseList module.
This module supplies override
"""


class VerboseList(list):
    def append(self, item):
        """Append an item to the end of the list and print a message
        indicating the addition.
        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, items):
        """Extend the list by appending all the items from the
        provided iterable and print a message indicating
        how many items were added.
        Args:
            items: An iterable of items to be added to the list.
        """
        num_items = len(items)
        super().extend(items)
        print(f"Extended the list with {[num_items]} items.")

    def remove(self, item):
        """Remove an item from the list and print a message
        before the removal.
        Args:
            item: The item to be removed from the list.
        """
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a message
        indicating which item was removed.
        If no index is specified, the last item is popped.
        Args:
            index: The index of the item to be popped. Default is -1,
            which pops the last item of the list.
        """
        item = super().pop(index)
        print(f"Popped {[item]} from the list.")
        return item
