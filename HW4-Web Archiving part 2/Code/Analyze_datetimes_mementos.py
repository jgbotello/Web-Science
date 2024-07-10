import json
import os
import gzip
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Directory where your TimeMaps JSON files are stored
directory = r"C:\Users\JHON G. BOTELLO\OneDrive - Old Dominion University\PHD\Courses\Spring 2024\Web Science\Web-Science\HW3-Web Archiving\get Timemaps\timemaps"

# Set the collection date (when you collected the TimeMaps)
collection_date = datetime.strptime("2024-06-04", "%Y-%m-%d")

# Lists to hold the data for the scatterplot
ages = []
memento_counts = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json.gz"):
        filepath = os.path.join(directory, filename)
        try:
            with gzip.open(filepath, 'rt', encoding='utf-8') as file:
                data = json.load(file)
                if 'mementos' in data and 'list' in data['mementos']:
                    # Extract the datetime of the earliest memento
                    earliest_memento = min(m['datetime'] for m in data['mementos']['list'])
                    earliest_memento_datetime = datetime.strptime(earliest_memento, "%Y-%m-%dT%H:%M:%SZ")
                    # Calculate the age in days
                    age = (collection_date - earliest_memento_datetime).days
                    # Count the number of mementos
                    memento_count = len(data['mementos']['list'])
                    # Append the data to the lists
                    ages.append(age)
                    memento_counts.append(memento_count)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Create a DataFrame for easier plotting
df = pd.DataFrame({
    'Age in Days': ages,
    'Number of Mementos': memento_counts
})

# Create the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age in Days'], df['Number of Mementos'], alpha=0.5)
plt.title('Scatterplot of Age of URI-Rs vs. Number of Mementos')
plt.xlabel('Age in Days')
plt.ylabel('Number of Mementos')
plt.grid(True)
plt.show()