from urllib.parse import urlparse
import requests
from time import time

# Checking if the URL is valid
def validate_url(url):
    if not isinstance(url, str):
        return False
    
    result = urlparse(url)
    valid_scheme = result.scheme in ("http", "https")
    valid_netloc = bool(result.netloc) and not result.netloc.startswith(':') and ':' not in result.netloc

    return valid_scheme and valid_netloc

## Fetching URL data
def fetch_url_data(url):
    start_time = time()
    try:
        response = requests.get(url, timeout=5)
        duration = int((time() - start_time) * 1000) 
        return {
            "url": url,
            "statusCode": response.status_code,
            "contentLength": int(response.headers.get('Content-Length', 0)),
            "requestDuration": f"{duration}ms",
            "date": response.headers.get('Date', "No date")
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "error": str(e)
        }