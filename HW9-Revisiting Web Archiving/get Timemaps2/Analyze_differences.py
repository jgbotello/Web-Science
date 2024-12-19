import json
import os
import gzip
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

directory_hw3 = r"C:/Users/JHON G. BOTELLO/OneDrive - Old Dominion University/PHD/Courses/Spring 2024/Web Science/Web-Science/HW3-Web Archiving/get Timemaps/timemaps"
directory_current = r"C:/Users/JHON G. BOTELLO/OneDrive - Old Dominion University/PHD/Courses/Spring 2024/Web Science/Web-Science/HW9-Revisiting Web Archiving/get Timemaps2/timemaps2"

def load_memento_counts_by_uri(directory):
    memento_counts = {}
    file_mapping = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json.gz"):
            filepath = os.path.join(directory, filename)
            try:
                with gzip.open(filepath, 'rt', encoding='utf-8') as file:
                    data = json.load(file)
                    if 'original_uri' in data and 'mementos' in data and 'list' in data['mementos']:
                        uri_r = data['original_uri']
                        memento_counts[uri_r] = len(data['mementos']['list'])
                        file_mapping[uri_r] = filename
                    else:
                        print(f"Unexpected JSON structure in file: {filename}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    return memento_counts, file_mapping

memento_counts_hw3, file_mapping_hw3 = load_memento_counts_by_uri(directory_hw3)
memento_counts_current, file_mapping_current = load_memento_counts_by_uri(directory_current)

# Calculate the differences and prepare a table
memento_data = []
for uri_r, count_hw3 in memento_counts_hw3.items():
    count_current = memento_counts_current.get(uri_r, 0) 
    difference = count_current - count_hw3
    file_hw3 = file_mapping_hw3.get(uri_r, "N/A")
    file_current = file_mapping_current.get(uri_r, "N/A")
    memento_data.append({
        "URI": uri_r,
        "HW3 Mementos": count_hw3,
        "Current Mementos": count_current,
        "Difference": difference,
        "HW3 File": file_hw3,
        "Current File": file_current
    })

df_mementos = pd.DataFrame(memento_data)

print(df_mementos)

output_csv_path = r"memento_comparison.csv"
df_mementos.to_csv(output_csv_path, index=False)

plt.figure(figsize=(10, 6))
sns.boxplot(x=df_mementos["Difference"], color="skyblue")
plt.title("Growth in Mementos Since July (HW3)", fontsize=14)
plt.xlabel("Difference in Mementos", fontsize=12)
plt.xticks(fontsize=10)
plt.xlim(df_mementos["Difference"].min(), df_mementos["Difference"].max())  # Limitar al rango real de diferencias
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

output_json_path = r"differences.json"
with open(output_json_path, "w") as output_file:
    json.dump(memento_data, output_file, indent=4)

print("Analysis complete. Boxplot displayed, and results saved to CSV and JSON files.")
