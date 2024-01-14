#!/usr/bin/env python3
"""Parameterize a unit test."""

import unittest
from parameterized import parameterized
import utils

class TestAccessNestedMap(unittest.TestCase):
    """Class for testing nested map access."""	
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the method returns what it is supposed to."""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
