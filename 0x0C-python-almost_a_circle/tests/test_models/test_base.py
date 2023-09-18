#!/usr/bin/python3
"""Unittest for Base module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest for constructor of base class"""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1, 1)
        self.assertEqual(base2, 2)

if __name__ == "__main__":
    unittest.main()