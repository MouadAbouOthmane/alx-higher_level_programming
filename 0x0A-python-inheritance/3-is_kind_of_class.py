#!/usr/bin/python3
"""3. Same class or inherit from TASK"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class ;
    otherwise False.
    """
    return isinstance(obj, a_class)
