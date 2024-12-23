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

directory_path = 'C:/Users/jbote001/OneDrive - Old Dominion University/PHD/Courses/Spring 2024/Web Science/Course/Homeworks_Solutions/HW3-Web Archiving/get Timemaps/timemaps'

compress_files_in_directory(directory_path)
