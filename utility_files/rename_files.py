import os
import glob

# Get a list of all directories starting with 'week'
directories = glob.glob('week*/')

for dir in directories:
    # Replace 'week' with 'project' in the directory name
    new_dir = dir.replace('week', 'project')
    
    # Rename the directory
    os.rename(dir, new_dir)