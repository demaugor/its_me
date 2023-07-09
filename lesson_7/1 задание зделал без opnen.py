import os
import sys
import shutil

os.mkdir('first')
os.mkdir('second')
os.mkdir('third')

file_path = os.path.abspath(sys.argv[0])

file_name = os.path.basename(file_path)

file_path_first = os.path.join('first', file_name)

shutil.copyfile(file_path, file_path_first)