import os
from pathlib import Path
import shutil

# Define the main directory
main_dir = Path("D:\Downloads")

# Check if the directory exists
if main_dir.exists() and main_dir.is_dir():
    contents = os.listdir(main_dir)
    ext = []

    # Extract extensions from filenames
    for f in contents:
        file_path = main_dir / f
        if file_path.is_file():  # Check if it's a file
            file_extension = file_path.suffix.lower()  # Get file extension (lowercase)
            if file_extension:  # Check if there's an extension
                ext.append(file_extension[1:])  # Remove the dot from the extension and add to list

    unique_ext = set(ext)
    print("Unique extensions:", unique_ext)

    # Create directories for each unique extension
    for e in unique_ext:
        ext_dir = main_dir / e
        if not ext_dir.exists():
            try:
                ext_dir.mkdir()
                print(f"Directory {ext_dir} created.")
            except OSError as error:
                print(f"Error creating directory {ext_dir}: {error}")
        else:
            print(f"Directory {ext_dir} already exists.")

    # Move files to corresponding directories
    for f in contents:
        file_path = main_dir / f
        if file_path.is_file():
            file_ext = file_path.suffix.lower()[1:]
            dest_dir = main_dir / file_ext
            if dest_dir.exists():
                try:
                    shutil.move(str(file_path), str(dest_dir))
                    print(f"Moved {file_path} to {dest_dir}")
                except shutil.Error as error:
                    print(f"Error moving {file_path} to {dest_dir}: {error}")
else:
    print("Directory 'test/' does not exist.")
