import os
import shutil

# Set the source directory path
source_dir = "D:\TDbrain\HEALTHY"

# Set the destination directory path
dest_dir = "D:\TDbrain\EO"

# Iterate through all subdirectories in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Construct the absolute path of the current file
        file_path = os.path.join(root, file)

        # Construct the new absolute path of the file in the destination directory
        dest_file_path = os.path.join(dest_dir, file)

        # Move the file to the destination directory and break out of the loop
        shutil.move(file_path, dest_file_path)
        break
