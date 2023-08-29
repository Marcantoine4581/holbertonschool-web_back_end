#!/usr/bin/env python3
"""Unittest for access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing the method access_nested_map """
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {'b': 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """  Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
       ({}, ("a",)),
       ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """  Test that a KeyError is raised for the following inputs """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
