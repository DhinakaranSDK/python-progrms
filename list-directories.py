import os

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
  print('Path: ' dirpath)
  print('Directory Name: ', dirnames)
  print('File Name: ', filenames)
  
