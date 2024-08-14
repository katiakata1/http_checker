import unittest
from unittest.mock import patch, Mock
import io
import sys
from src.main import main

class TestMainFunction(unittest.TestCase):

    @patch('src.utils.fetch_url_data')
    @patch('src.utils.validate_url')
    @patch('sys.stdin', new_callable=io.StringIO)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.stferr', new_callable=io.StringIO)
    def test_main_valid_urls(self, mock_stdin, mock_stdout, mock_stderr, mock_validate_url, mock_fetch_url_data):
        mock_stdin.write('https://www.example.com\n')
        mock_stdin.seek(0)

        mock_validate_url.return_value=True
        mock_fetch_url_data.return_value = {
            'url': 'https://www.example.com',
            'statusCode' : 200,
            'contentLength' : 1234,
            'requestDuration': '50ms',
            'date' : 'Mon, 01 Jan 2024 00:00:00 GMT'
        }

        main()

        self.assertIn('https://www.example.com', mock_stdout.getvalue())
        self.assertIn('200', mock_stdout.getvalue())
        self.assertIn('1234', mock_stdout.getvalue())
        self.assertIn('50ms', mock_stdout.getvalue())
        self.assertIn('Mon, 01 Jan 2024 00:00:00 GMT', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()