# -*- coding:utf-8 -*-

"""User representation."""


class User(object):
    """Object representation of user."""

    def __init__(self, name: str, age: int):
        """Construct a new user."""
        self.name = name
        self.age = age

    def get_introduction(self) -> str:
        """Return a user's self-introduction."""
        return "Hello, i'm {user.name}, {user.age}".format(user=self)
