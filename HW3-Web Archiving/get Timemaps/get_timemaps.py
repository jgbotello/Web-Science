import subprocess
import os
import hashlib
import time

# Nombre del archivo que contiene las URIs
input_file = "collected_uris.txt"

# Carpeta donde se guardarán los TimeMaps
output_folder = "timemaps"

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Comando base de Memgator
memgator_cmd = "memgator-windows-amd64 -a https://raw.githubusercontent.com/odu-cs432-websci/public/main/archives.json -F 2 -f JSON"

# Leer el archivo de URIs y recuperar los TimeMaps
with open(input_file, "r") as f:
    for uri in f:
        uri = uri.strip()  # Eliminar espacios en blanco
        md5_hash = hashlib.md5(uri.encode()).hexdigest()  # Calcular hash MD5
        output_file = os.path.join(output_folder, f"timemap_{md5_hash}.json")  # Nombre del archivo de salida
        subprocess.run(f"{memgator_cmd} {uri} > {output_file}", shell=True)  # Ejecutar el comando
        print(f"TimeMap retrieved for URI {uri} with hash {md5_hash}")
        time.sleep(15)  # Esperar 15 segundos entre llamadas

print("All TimeMaps retrieved and saved in the 'timemaps' folder.")
