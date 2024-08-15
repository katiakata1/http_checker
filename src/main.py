import sys
import os
import json

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.utils import validate_url, fetch_url_data


def main():
    input_stream = sys.stdin
    output_stream = sys.stdout
    error_stream = sys.stderr

    results = []

    for line in input_stream:
        url = line.strip()

        if validate_url(url):
            try:
                data = fetch_url_data(url)
                if 'error' in data:
                    result = {
                        'url': url,
                        'error': data['error']
                    }
                else:
                    result = {
                        'url': data['url'],
                        'statusCode': data['statusCode'],
                        'contentLength': data['contentLength'],
                        'requestDuration': data['requestDuration'],
                        'date': data['date']
                    }
                    results.append(result)
            except Exception as e:
                results.append({
                    'url': url,
                    'error': f'An unexpected error occurred: {str(e)}'
                })
        else:
            results.append({
                'url': url,
                'error': 'invalid url'
            })
    
    json.dump(results, output_stream, indent=2)

if __name__ == "__main__":
    main()