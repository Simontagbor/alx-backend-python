#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_client = GithubOrgClient(org_name)
        response = test_client.org
        self.assertEqual(response, {"payload": True})
        mock_get_json.\
            assert_called_once_with(
                    f'https://api.github.com/orgs/{org_name}')

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url
        returns the expected result."""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload
        test_client = GithubOrgClient('google')
        self.assertEqual(test_client._public_repos_url, payload["repos_url"])
        mock_org.assert_called_once()

    @patch('client.get_json', return_value=["repo1", "repo2"])
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos
        returns the expected result."""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value =\
                 "https://api.github.com/orgs/google/repos"
            test_client = GithubOrgClient('google')
            self.assertEqual(test_client.public_repos, ["repo1", "repo2"])
            mock_get_json.\
                assert_called_once_with(mock_public_repos_url.return_value)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
     ({"license": {"key": "my_license"}}, "my_license", True),
     ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test that GithubOrgClient.has_license
        returns the expected result."""
        test_client = GithubOrgClient('google')
        self.assertEqual(test_client.has_license(repo, license_key),
                         expected_result)


@parameterized_class([
    {"org_payload": fixtures.org_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos,
     "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.expected_repos, cls.apache2_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        cls.get_patcher.stop()
