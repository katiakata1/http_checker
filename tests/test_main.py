import unittest
from unittest.mock import patch, Mock
import io
import sys
from src.main import main
import json

class TestMainFunction(unittest.TestCase):

    @patch('src.main.fetch_url_data')
    @patch('src.main.validate_url')
    @patch('sys.stdin', new_callable=io.StringIO)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.stderr', new_callable=io.StringIO)
    def test_main_valid_urls(self, mock_stderr, mock_stdout, mock_stdin, mock_validate_url, mock_fetch_url_data):
        mock_stdin.write('https://www.example.com\nbad://address\nhttp://not.exists.bbc.co.uk/\n')
        mock_stdin.seek(0)

        mock_validate_url.side_effect = [True, False, True]  # First URL valid, second invalid, third valid
        mock_fetch_url_data.side_effect = [
            {  # Successful fetch for first URL
                'url': 'https://www.example.com',
                'statusCode': 200,
                'contentLength': 1234,
                'requestDuration': '50ms',
                'date': 'Mon, 01 Jan 2024 00:00:00 GMT'
            },
            # No need to specify for invalid URL, mock_validate_url returns False
            {
                'url': 'http://not.exists.bbc.co.uk/',
                'error': 'HTTPConnectionPool(host=\'not.exists.bbc.co.uk\', port=80): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x100985160>: Failed to resolve \'not.exists.bbc.co.uk\' ([Errno 8] nodename nor servname provided, or not known)"))'
            }
        ]

        main()

        output = mock_stdout.getvalue().strip()
        stderr = mock_stderr.getvalue().strip()
        results = json.loads(output)

        expected_results = [
            {
                'url': 'https://www.example.com',
                'statusCode': 200,
                'contentLength': 1234,
                'requestDuration': '50ms',
                'date': 'Mon, 01 Jan 2024 00:00:00 GMT'
            },
            {
                'url': 'bad://address',
                'error': 'invalid url'
            },
            {
                'url': 'http://not.exists.bbc.co.uk/',
                'statusCode': 504,
                'date': 'Wed, 19 Jun 2024 15:16:33 GMT'
            }
        ]

        # Validate results
        self.assertEqual(len(results), len(expected_results), "Output length mismatch")
        for expected, result in zip(expected_results, results):
            self.assertEqual(expected, result, f"Expected {expected} but got {result}")

        # Validate errors
        self.assertIn('Invalid URL: bad://address', stderr)
        self.assertIn('Error fetching data for http://not.exists.bbc.co.uk/:', stderr)




if __name__ == '__main__':
    unittest.main()