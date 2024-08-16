# URL Checker Project

## Overview

This project is a command-line tool that reads a list of URLs, validates them, fetches their status and content, and outputs the results as a JSON document. The development process was guided by a test-first approach, ensuring robust and reliable code.

## Repository Structure

Here's a brief overview of the repository structure:
```bash
|-- src/
|   |-- main.py          # The main script that processes URLs and outputs the results as JSON.
|   |-- utils.py         # Utility functions, including URL validation and fetching logic.
|
|-- tests/
|   |-- test_main.py     # Unit tests for the main function.
|   |-- test_utils.py    # Unit tests for utility functions (validation and fetching).
|
|-- urls.txt             # Sample input file containing URLs to be processed.
|-- output.json          # Sample output JSON (generated after running the script).
|-- error_log.txt        # Sample error log (generated after running the script with error redirection).
```

## Development Process

The development process for this project followed a test-driven development (TDD) methodology. Below are the key steps taken to build the application:

### 1. URL Validation

**Step 1: Creating the Unit Test for URL Validation**

The first step was to write a unit test to ensure that the URL validation logic correctly identifies valid and invalid URLs. This was done using the `unittest` framework.

- **Test Class**: `TestURLValidation`
- **Purpose**: Ensure that the `validate_url` function correctly validates URLs.

**Step 2: Implementing the URL Validation Function**

After the test was written, the `validate_url` function was implemented to pass the test. This function checks if a given URL is well-formed and can be processed further.

- **Function**: `validate_url`
- **Purpose**: Validate the format of the URL.

### 2. URL Fetching

**Step 1: Creating the Unit Test for URL Fetching**

Once the URL validation was complete, the next step was to write a unit test for the URL fetching functionality. This test was designed to check if the application could correctly fetch data from valid URLs and handle errors for invalid or unreachable URLs.

- **Test Class**: `TestURLFetching`
- **Purpose**: Ensure that the `fetch_url_data` function correctly handles both successful and failed fetch attempts.

**Step 2: Implementing the URL Fetching Function**

After writing the test, the `fetch_url_data` function was implemented. This function uses HTTP requests to fetch the status code, content length, and other metadata for a given URL.

- **Function**: `fetch_url_data`
- **Purpose**: Fetch data from a URL, including status code and content length.

### 3. Main Function: Processing and Outputting Data

**Step 1: Creating the Unit Test for the Main Function**

With URL validation and fetching in place, the next step was to write a unit test for the main function. This test ensures that the main function processes the input URLs, fetches their data, and outputs the results as a JSON document.

- **Test Class**: `TestMainFunction`
- **Purpose**: Ensure that the main function processes data correctly and outputs a valid JSON document.

**Step 2: Implementing the Main Function**

After the test was written, the main function was implemented to pass the test. The function reads URLs from standard input, validates them, fetches their data, and outputs the results as a JSON document.

- **Function**: `main`
- **Purpose**: Process input URLs, fetch data, and output the results as a JSON document.

## Usage

To run the program, you can use the following command:

```bash
python3 src/main.py < urls.txt > output.json
```

## Error Output

```bash
python3 src/main.py < urls.txt 2> error_log.txt
```

## Testing
```bash
python3 -m unittest discover -s tests
```



