import os
import time
import sys

a = float(sys.argv[1])
population_size = int(a)
optimizer_output = 'optimizer_output/mesh_files'
total_mesh_file = 0


while (total_mesh_file < population_size):
    for root, dirs, files in os.walk(optimizer_output, topdown=False):
        total_mesh_file = len(files)
    time.sleep(2)

print('All mesh files are generated...')
