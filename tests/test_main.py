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
        mock_stdin.write('https://www.example.com\n')
        mock_stdin.seek(0)

        mock_validate_url.return_value = True
        mock_fetch_url_data.return_value = {
            'url': 'https://www.example.com',
            'statusCode' : 200,
            'contentLength': 1234,
            'requestDuration': '50ms',
            'date' : 'Mon, 01 Jan 2024 00:00:00 GMT'
        }

        main()

        # output = mock_stdout.getvalue()
        output = mock_stdout.getvalue().strip()
        results = json.loads(output)

        # self.assertIn('https://www.example.com', output)
        # self.assertIn('200', output)
        # self.assertIn('1234', output)
        # self.assertIn('50ms', output)
        # self.assertIn('Mon, 01 Jan 2024 00:00:00 GMT', output)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['url'], 'https://www.example.com')
        self.assertEqual(results[0]['statusCode'], 200)
        self.assertEqual(results[0]['contentLength'], 1234)
        self.assertEqual(results[0]['requestDuration'], '50ms')
        self.assertEqual(results[0]['date'], 'Mon, 01 Jan 2024 00:00:00 GMT')

        # Check that no errors were written to stderr
        self.assertEqual(mock_stderr.getvalue(), '')


if __name__ == '__main__':
    unittest.main()