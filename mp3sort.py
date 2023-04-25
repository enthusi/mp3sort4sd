import shutil
import os
from pathlib import Path

#essentially based on this
#https://rowannicholls.github.io/python/utilities/cut_copy_files.html

# Source folder
src_folder = '.'
dst_folder = '/run/media/mountpoint'

for dirpath, dirnames, filenames in os.walk(src_folder):
    dirnames.sort()
    filenames.sort()
    for filename in filenames:
        # Ignore hidden files
        if filename.startswith('.'):
            continue
        # Only move one type of file
        if not filename.endswith('.mp3'):
            continue
        src_path = Path(dirpath, filename)
        dst_dirpath = dirpath.replace(str(src_folder), dst_folder, 1)
        dst_path = Path(dst_dirpath, filename)
        # Check that the destination folder exists (create it if not)
        os.makedirs(dst_dirpath, exist_ok=True)
        # Copy file
        print(f'Copying "{src_path}" to "{dst_path}"')
        shutil.copy(src_path, dst_path)
