import os

# About OS moduel
print(dir(os))

# Print current working directory
print(os.getcwd())

# Changing directory
os.chdir('Directory')

# List directory
print(os.listdir())

# Making Directory
os.mkdir('New-Directory') # Makes only parent directory
os.makedirs('Parent-Directory/Sub-Directory') # Make subdirectory also

# Remove Directory
os.rmdir('New-Directory') # Removes mentioned directory
os.removedirs('Parent-Directory/Sub-Directory') # Removes subdirectory also

# Rename file
os.rename('Source File Name', 'Dest File Name')

# File information
print(os.stat('File name'))

# Print Directories, Sub Directories and Files
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
  print('Path: ' dirpath)
  print('Directory Name: ', dirnames)
  print('File Name: ', filenames)
  
# Environment variable
print(os.environ)

# Path join 
file_path = os.path.join('', '')

# Base name 
print(os.path.basename('path'))

# Dir name 
print(os.path.dirname(''))

# Split path with base name and dir name
print(os.path.split('path')) #Gives list with first base name followed by dir name

# Path exist
print(os.path.exists('path))

# Chech is directory
print(os.path.isdir('path'))
                     
# Chech is file
print(os.path.isfile('path'))
                     
# Split as root and extension
print(os.path.splitext('path'))
