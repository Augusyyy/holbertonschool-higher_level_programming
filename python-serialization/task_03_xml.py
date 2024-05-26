#!/usr/bin/python3
"""xml serialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML data.

    Returns:
    None
    """
    # Create the root element
    root = ET.Element('data')

    # Helper function to recursively add dictionary items to the XML tree
    def build_tree(element, dictionary):
        for key, value in dictionary.items():
            # Create a new element for each key
            child = ET.SubElement(element, key)
            if isinstance(value, dict):
                # If the value is a dictionary, recursively add its items
                build_tree(child, value)
            else:
                # Otherwise, set the text of the element to the value
                child.text = str(value)

    # Build the XML tree from the dictionary
    build_tree(root, dictionary)

    # Create an ElementTree object and write it to the file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Parameters:
    filename (str): The name of the XML file to read.

    Returns:
    dict: The deserialized dictionary.
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Helper function to recursively convert XML elements to dictionary items
    def parse_element(element):
        # If the element has children, parse them recursively
        if len(element):
            return {child.tag: parse_element(child) for child in element}
        else:
            # If the element is a leaf, return its text content
            return element.text

    # Build the dictionary from the root element
    elements = parse_element(root)
    return elements
