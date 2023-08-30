#!/usr/bin/env python3
"""Unittest for client.py
"""
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
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


    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url is the expected one
        based on the mocked payload """
        with patch('client.GithubOrgClient.org',
                    new_callable=PropertyMock) as mock:
            payload = {"repos_url": "url"}
            mock.return_value = payload
            test_class = GithubOrgClient('anything here')
            result = test_class._public_repos_url
            mock.assert_called_once()
            self.assertEqual(result, payload["repos_url"])
