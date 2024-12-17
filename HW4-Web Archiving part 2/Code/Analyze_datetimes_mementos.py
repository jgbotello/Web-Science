import json
import os
import gzip
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

directory = r"C:\Users\JHON G. BOTELLO\OneDrive - Old Dominion University\PHD\Courses\Spring 2024\Web Science\Web-Science\HW3-Web Archiving\get Timemaps\timemaps"

collection_date = datetime.strptime("2024-07-10", "%Y-%m-%d")

ages = []
memento_counts = []
uri_list = []

oldest_memento_date = collection_date
oldest_memento_uri = None

uris_less_than_one_week = 0

for filename in os.listdir(directory):
    if filename.endswith(".json.gz"):
        filepath = os.path.join(directory, filename)
        try:
            with gzip.open(filepath, 'rt', encoding='utf-8') as file:
                data = json.load(file)
                if 'mementos' in data and 'list' in data['mementos']:
                    earliest_memento = min(m['datetime'] for m in data['mementos']['list'])
                    earliest_memento_datetime = datetime.strptime(earliest_memento, "%Y-%m-%dT%H:%M:%SZ")
                    age = (collection_date - earliest_memento_datetime).days
                    memento_count = len(data['mementos']['list'])
                    ages.append(age)
                    memento_counts.append(memento_count)
                    uri_list.append(data['original_uri'])

                    if earliest_memento_datetime < oldest_memento_date:
                        oldest_memento_date = earliest_memento_datetime
                        oldest_memento_uri = data['original_uri']

                    if age < 7:
                        uris_less_than_one_week += 1
        except Exception as e:
            print(f"Error processing file {filename}: {e}")


df = pd.DataFrame({
    'URI': uri_list,
    'Age in Days': ages,
    'Number of Mementos': memento_counts
})

# Analysis and output
print(f"The URI-R with the oldest memento is: {oldest_memento_uri}")
print(f"The date of the oldest memento is: {oldest_memento_date}")
print(f"Number of URI-Rs with an age of less than 1 week: {uris_less_than_one_week}")

# Relationship analysis
correlation = df['Age in Days'].corr(df['Number of Mementos'])
print(f"Correlation between age of URI-R and number of mementos: {correlation}")

# Creating the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age in Days'], df['Number of Mementos'], alpha=0.5)
plt.title('Scatterplot of Age of URI-Rs vs. Number of Mementos')
plt.xlabel('Age in Days')
plt.ylabel('Number of Mementos')
plt.grid(True)
plt.show()