import os
import glob

# Get a list of all directories
directories = glob.glob('*/')

for dir in directories:
    # Create a new path for the 'design' directory
    new_dir = os.path.join(dir, 'design')
    
    # Create the 'design' directory
    os.makedirs(new_dir, exist_ok=True)