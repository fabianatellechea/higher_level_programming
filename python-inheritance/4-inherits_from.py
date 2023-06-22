#!/usr/bin/python3
""" returns True if the object is an instance of class
that inherited (directly or indirectly)from the class """


def inherits_from(obj, a_class):
    """function """
    return issubclass(type(obj), a_class) and type(obj) != a_class
