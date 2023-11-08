import linecache
import json
import requests

# Set the range of lines you want to process.
start = 1
end = 50
i = start

while i <= end:
    try:
        # Read a specific line from the 'output.txt' file.
        line = linecache.getline('./output.txt', i)

        # Check if the line is empty (not found).
        if not line:
            print(f"Line {i} not found in 'output.txt'")
            i += 1
            continue

        # Parse the line as JSON data.
        myjson = json.loads(line)
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors.
        print(f"Error decoding JSON at line {i}: {str(e)}")
        i += 1
        continue

    try:
        # Make an HTTP POST request with the JSON data.
        response = requests.post('http://localhost:80/invoiceitem', json=myjson)
        response.raise_for_status()
        print("Status code:", response.status_code)
        print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors.
        print("HTTP Request Error:", str(e))

    i += 1