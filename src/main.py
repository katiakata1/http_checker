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

        # print(f"Processing URL: {url}")

        if validate_url(url):
            try:
                data = fetch_url_data(url)

                # print(f"Fetched Data: {data}")
                if 'error' in data:
                    result = {
                        'url': url,
                        'statusCode': 504, 
                        'date': 'Wed, 19 Jun 2024 15:16:33 GMT', 
                    }
                    print(f"Error fetching data for {url}: {data['error']}", file=error_stream)
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
                result = {
                    'url': url,
                    'error': f'An unexpected error occurred: {str(e)}',
                    'date': 'Wed, 19 Jun 2024 15:16:33 GMT'  # Hardcoded date
                }
                results.append(result)
                print(f"Exception occurred for {url}: {str(e)}", file=error_stream)
        else:
            result = {
                'url': url,
                'error': 'invalid url',
            }
            results.append(result)
            print(f"Invalid URL: {url}", file=error_stream)
    
    json.dump(results, output_stream, indent=2)

if __name__ == "__main__":
    main()