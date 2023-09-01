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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Test that the list of repos is what you expect from the chosen
        payload """
        json_payload = [{"name": "Google"}, {"name": "abc"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "string"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [repo["name"] for repo in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()
