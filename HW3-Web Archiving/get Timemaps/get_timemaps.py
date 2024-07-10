import subprocess
import os
import hashlib
import time

# Name of the file containing the URIs
input_file = "collected_uris.txt"

# Folder where I will save the TimeMaps
output_folder = "timemaps"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Execute memgator
memgator_cmd = "memgator-windows-amd64 -a https://raw.githubusercontent.com/odu-cs432-websci/public/main/archives.json -F 2 -f JSON"

with open(input_file, "r") as f:
    for uri in f:
        uri = uri.strip()  # Eliminate blank spaces
        md5_hash = hashlib.md5(uri.encode()).hexdigest()  # for hash
        output_file = os.path.join(output_folder, f"timemap_{md5_hash}.json")  # Name for the file
        subprocess.run(f"{memgator_cmd} {uri} > {output_file}", shell=True)
        print(f"TimeMap retrieved for URI {uri} with hash {md5_hash}")
        time.sleep(15)  # Add time sleep

print("All TimeMaps retrieved and saved in the 'timemaps' folder.")
