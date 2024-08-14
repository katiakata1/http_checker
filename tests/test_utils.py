import unittest
from src.utils import validate_url

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

if __name__ == '__main__':
    unittest.main()
