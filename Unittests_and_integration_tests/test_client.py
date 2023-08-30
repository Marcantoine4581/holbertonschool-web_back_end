#!/usr/bin/env python3
"""Unittest for client.py
"""
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing the method test_org """
    @parameterized.expand([
       ('google'),
       ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ Test the method org """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
