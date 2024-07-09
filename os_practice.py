import os
from pathlib import Path
import shutil

# Check if the directory exists
if os.path.exists("test/"):
    contents = os.listdir("test/")
    ext = []

    # Extract extensions from filenames
    for f in contents:
        if os.path.isfile(f"test/{f}"):     # Check if it's a file
            file_extension = Path(f).suffix.lower()     # Get file extension (lowercase)
            # print(file_extension)
            if file_extension:      # Check if there's an extension
                ext.append(file_extension[1:])      # Remove the dot from the extension and add to list

    unique_ext = set(ext)
    print(unique_ext)

    # Create directories for each unique extension
    for e in unique_ext:
        if not os.path.exists(f"test/{e}"):
            try:
                os.mkdir(f"test/{e}")
            except OSError as e:
                print(f"Error creating directory test/{e}: {e}")
        else:
            print(f"Directory test/{e} already exists.")

    def file_O(f):
        if os.Path.isfile(f):
            return True
    
    # print(contents)
    # file_only = filter(file_O,contents)
    file_only = list(filter(lambda f: os.path.isfile(f"test/{f}"),contents))
    
    for index,f in enumerate(file_only):
        src = f"test/{f}"
        file_ext = f.split('.')[-1]

        for e in unique_ext:
            if file_ext == e:
                dest = f"test/{e}/"
                shutil.move(src,dest)
            
else:
    print("Directory 'test/' does not exist.")
