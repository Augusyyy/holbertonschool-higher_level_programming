#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This is the Storage module.
This module supplies abstractmethod
"""


class Storage(ABC):
    @abstractmethod
    def store(self, item):
        """
        Store the given item.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def retrieve(self, item):
        """
        Retrieve the given item.
        This method must be implemented by subclasses.
        """
        pass


# Implementing Warehouse and Vault
class Warehouse(Storage):
    def __init__(self):
        """
        Initialize the warehouse with an empty list to hold items.
        """
        self.items = []

    def store(self, item):
        """
        Store the item in the warehouse.
        """
        self.items.append(item)
        print(f"Item '{item}' stored in the warehouse.")

    def retrieve(self, item):
        """
        Retrieve the item from the warehouse.
        If the item is found, remove it from the list and return it.
        Otherwise, return None.
        """
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' retrieved from the warehouse.")
            return item
        print(f"Item '{item}' not found in the warehouse.")
        return None


class Vault(Storage):
    def __init__(self):
        """
        Initialize the vault with an empty list to hold items.
        """
        self.items = []

    def store(self, item):
        """
        Store the item in the vault with extra security checks.
        """
        print("Performing security checks...")
        self.items.append(item)
        print(f"Item '{item}' stored in the vault with extra security.")

    def retrieve(self, item):
        """
        Retrieve the item from the vault with extra security checks.
        If the item is found, remove it from the list and return it.
        Otherwise, return None.
        """
        print("Performing security checks...")
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' retrieved from the vault.")
            return item
        print(f"Item '{item}' not found in the vault.")
        return None


# Building the InventorySystem
class InventorySystem:
    def __init__(self, storage: Storage):
        """
        Initialize the inventory system with the given storage.
        """
        self.storage = storage

    def add_item(self, item):
        """
        Add the item to the storage.
        """
        self.storage.store(item)

    def get_item(self, item):
        """
        Get the item from the storage.
        """
        return self.storage.retrieve(item)
