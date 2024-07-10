import json
import os
import gzip
from collections import Counter

# Directory where my TimeMaps JSON files are stored
directory = r"C:\Users\JHON G. BOTELLO\OneDrive - Old Dominion University\PHD\Courses\Spring 2024\Web Science\Web-Science\HW3-Web Archiving\get Timemaps\timemaps"

# Initialize counters
memento_counts = Counter()
max_mementos = 0
uri_with_max_mementos = None
file_with_max_mementos = None

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json.gz"):
        filepath = os.path.join(directory, filename)
        try:
            with gzip.open(filepath, 'rt', encoding='utf-8') as file:
                data = json.load(file)
                # Check if data is loaded correctly
                if 'mementos' in data and 'list' in data['mementos']:
                    # Count the mementos for the URI-R
                    memento_count = len(data['mementos']['list'])  # Number of mementos
                    memento_counts[memento_count] += 1
                    # Update max_mementos and uri_with_max_mementos if this URI-R has more mementos
                    if memento_count > max_mementos:
                        max_mementos = memento_count
                        uri_with_max_mementos = data['original_uri']
                        file_with_max_mementos = filename
                else:
                    print(f"Unexpected JSON structure in file: {filename}")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Convert the counter to a sorted list of tuples (sorting this)
memento_distribution = sorted(memento_counts.items())

# Print the result
print("Mementos | URI-Rs")
print("----------------")
for mementos, count in memento_distribution:
    print(f"{mementos:<8} | {count}")

# Print the URI-R with the most mementos and the file name
print(f"\nThe URI-R with the most mementos is: {uri_with_max_mementos}")
print(f"Number of mementos: {max_mementos}")
print(f"File name: {file_with_max_mementos}")
