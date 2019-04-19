# -*- coding:utf-8 -*-

"""Users representation tests."""

import unittest

from hexlet_python_package.user import User


class TestUser(unittest.TestCase):
    """Tests the User class routines."""

    def test_instantiation(self):
        """Check that User instance has the particular properties."""
        bob = User('Bob', 42)
        self.assertEqual(bob.name, 'Bob')
        self.assertEqual(bob.age, 42)

    def test_introduction(self):
        """Check that user introduses herself properly."""
        alice = User('Alice', 21)
        intro = alice.get_introduction()
        self.assertIn('Alice', intro)
        self.assertIn(str(21), intro)
