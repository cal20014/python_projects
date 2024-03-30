
import os
import glob
import shutil

# Get a list of all .pdf files in all directories
pdf_files = glob.glob('*/*.pdf')

for file in pdf_files:
    # Get the parent directory of the file
    parent_dir = os.path.dirname(file)
    
    # Create a new path for the 'design' directory
    design_dir = os.path.join(parent_dir, 'design')
    
    # Create the 'design' directory if it doesn't exist
    os.makedirs(design_dir, exist_ok=True)
    
    # Create a new path for the file in the 'design' directory
    new_file_path = os.path.join(design_dir, os.path.basename(file))
    
    # Move the file to the 'design' directory
    shutil.move(file, new_file_path)