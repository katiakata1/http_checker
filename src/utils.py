from urllib.parse import urlparse

def validate_url(url):
    if not isinstance(url, str):
        return False
    
    result = urlparse(url)
    print(f"Parsing URL: {url}")
    print(f"Scheme: {result.scheme}")
    print(f"Netloc: {result.netloc}")

    # Ensure that scheme is either 'http' or 'https'
    valid_scheme = result.scheme in ("http", "https")
    
    # Ensure that netloc is not empty and contains a valid hostname
    valid_netloc = bool(result.netloc) and not result.netloc.startswith(':') and ':' not in result.netloc

    return valid_scheme and valid_netloc