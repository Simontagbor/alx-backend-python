#!/usr/bin/env python3
"""Parameterize a unit test."""

import unittest
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ({"a": 1}, ("b",)),
        ({"a": {"b": 2}}, ("a", "c")),
        ({"a": {"b": 2}}, ("a", "b", "c"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised for certain paths."""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for testing utils.get_json."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns the expected result."""
        mock_get.return_value = Mock(json=lambda: test_payload)
        result = utils.get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """Test that when calling a_property twice,
        the correct result is returned but
        a_method is only called once."""

        class TestClass:
            """Test class for memoization."""
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            test_class_instance = TestClass()
            self.assertEqual(test_class_instance.a_property, 42)
            self.assertEqual(test_class_instance.a_property, 42)
            mock_a_method.assert_called_once()
