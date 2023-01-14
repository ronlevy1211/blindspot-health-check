import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from models.HealthCheck.HealthCheck import HealthCheck


class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.package = HealthCheck("test")

    def test_check_version_date(self):
        self.package.package.date = (datetime.now() - timedelta(days=29)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.assertEqual(self.package.check_version_date(), True)

        self.package.package.date = (datetime.now() - timedelta(days=31)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.assertEqual(self.package.check_version_date(), False)

    def test_check_maintainers(self):
        self.package.package.maintainers = ["Ron Levy"]
        self.assertEqual(self.package.check_maintainers(), False)

        self.package.package.maintainers = ["Ron Levy", "Amit Hangel"]
        self.assertEqual(self.package.check_maintainers(), True)

    @patch('requests.get')
    def test_check_repository_commit(self, mock_get):
        last_commit_date = (datetime.now() - timedelta(days=13)).strftime("%Y-%m-%dT%H:%M:%SZ")
        mock_response = MagicMock()
        mock_response.json.return_value = [{
            "commit": {
                "committer": {
                    "date": last_commit_date
                }
            }
        }]
        mock_get.return_value = mock_response
        self.package.package.repository_url = "https://github.com/test/test.git"
        result = self.package.check_repository_commit()
        self.assertTrue(result)

        last_commit_date = (datetime.now() - timedelta(days=15)).strftime("%Y-%m-%dT%H:%M:%SZ")
        mock_response.json.return_value = [{
            "commit": {
                "committer": {
                    "date": last_commit_date
                }
            }
        }]
        result = self.package.check_repository_commit()
        self.assertFalse(result)
