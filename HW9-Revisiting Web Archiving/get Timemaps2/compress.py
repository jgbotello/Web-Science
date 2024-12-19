# Script to compress my files
import os
import gzip
import shutil

def compress_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            compressed_file_path = file_path + '.gz'
            
            with open(file_path, 'rb') as f_in:
                with gzip.open(compressed_file_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

# Directory to save my files
directory_path = 'C:/Users/JHON G. BOTELLO/OneDrive - Old Dominion University/PHD/Courses/Spring 2024/Web Science/Web-Science/HW9-Revisiting Web Archiving/get Timemaps2/timemaps2'

# Compress all files in the directory
compress_files_in_directory(directory_path)
