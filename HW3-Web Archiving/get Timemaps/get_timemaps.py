import subprocess
import os

input_file = "collected_uris.txt"

output_folder = "timemaps"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

memgator_cmd = "memgator-windows-amd64 -a https://raw.githubusercontent.com/odu-cs432-websci/public/main/archives.json -F 2 -f JSON"

with open(input_file, "r") as f:
    for i, uri in enumerate(f, start=1):
        uri = uri.strip()  
        output_file = os.path.join(output_folder, f"timemap_{i}.json")  
        subprocess.run(f"{memgator_cmd} {uri} > {output_file}", shell=True)
        print(f"TimeMap retrieved for URI {i}: {uri}")

print("All TimeMaps retrieved and saved in the 'timemaps' folder.")