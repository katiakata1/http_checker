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

    for line in input_stream:
        url = line.strip()

        results = []

        if validate_url(url):
            try:
                data = fetch_url_data(url)
                if 'error' in data:
                    error_stream.write(f"Failed to fetch data for {url}: {data['error']}\n")
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
                error_stream.write(f"An unexpected error occurred for {url}: {str(e)}\n")
        else:
            error_stream.write(f"Invalid URL: {url}\n")
    
    json.dump(results, output_stream, indent=2)

if __name__ == "__main__":
    main()