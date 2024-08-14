import unittest
from unittest.mock import patch, Mock
import requests
from src.utils import validate_url, fetch_url_data

## Checking if the URL is valid
class TestUtils(unittest.TestCase):
    def test_validate_url_success(self):
        valid_urls = [
            "http://www.example.com",
            "https://www.example.com",
            "http://subdomain.example.com",
            "https://example.com/path?query=1"
        ]
        for url in valid_urls:
            self.assertTrue(validate_url(url))

    def test_validate_url_failure(self):
        invalid_urls = [
            "htp://www.example.com",  # Wrong scheme
            "www.example.com",         # Missing scheme
            "http://",                 # Missing netloc
            "https://:80"              # Missing netloc
        ]
        for url in invalid_urls:
            self.assertFalse(validate_url(url))


## Checking for URL fetching with mock http request
class TestFetchUrlData(unittest.TestCase):

    @patch('src.utils.requests.get')
    def test_fetch_url_data_success(self, mock_get):
        # Mock a successful HTTP response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Length': '1234', 'Date': 'Mon, 01 Jan 2024 00:00:00 GMT'}
        mock_get.return_value = mock_response

        url = "https://www.example.com"
        result = fetch_url_data(url)

        self.assertEqual(result['url'], url)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['contentLength'], 1234)
        self.assertTrue(result['requestDuration'].endswith("ms"))
        self.assertEqual(result['date'], 'Mon, 01 Jan 2024 00:00:00 GMT')

    @patch('src.utils.requests.get')
    def test_fetch_url_data_failure(self, mock_get):
        # Mock a failed HTTP request
        mock_get.side_effect = requests.exceptions.RequestException("Error")

        url = "https://www.nonexistentwebsite.com"
        result = fetch_url_data(url)

        self.assertEqual(result['url'], url)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
