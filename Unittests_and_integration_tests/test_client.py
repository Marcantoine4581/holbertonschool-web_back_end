#!/usr/bin/env python3
"""Unittest for client.py
"""
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing the method test_org, test_public_repos_url,
    test_public_repos, test_has_license """
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for testing the public_repos method in an integration test """
    @classmethod
    def setUpClass(cls):
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test for the method public_repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("UNKNOWN_LICENCE"), [])
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()
