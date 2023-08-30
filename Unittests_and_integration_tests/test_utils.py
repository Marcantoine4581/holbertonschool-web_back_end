#!/usr/bin/env python3
"""Unittest for access_nested_map
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """ Class for testing the method get_json """
    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test the method get_json """
        #  Instantiate a new Mock instance
        response_mock = Mock()
        response_mock.json.return_value = test_payload
        with patch("requests.get", return_value=response_mock):
            response = get_json(test_url)
            response_mock.json.assert_called_once()
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Class for testing the method memoize """
    def test_memoize(self):
        """ Test the method memoize """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_method.assert_called_once()
