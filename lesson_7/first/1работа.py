import os
import sys

os.mkdir('first')
os.mkdir('second')
os.mkdir('third')

file_path = os.path.abspath(sys.argv[0])

file_name = os.path.basename(file_path)

with open(file_path, 'r') as f:
    file_content = f.read()

file_path_first = os.path.join('first', file_name)

with open(file_path_first, 'w') as f:
    f.write(file_content)