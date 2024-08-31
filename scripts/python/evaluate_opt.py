import os
import os, glob, re

result_dir = "result"
file_count = 0

consistency_checked = 0
for file in glob.glob(result_dir + "/result-*"):
    file_pointer = open(file)
    nmuses = []
    ntimes = [] 
    file_count += 1
    for line in file_pointer:
        if line.startswith("Models"):
            l = line.split()
            nmuses.append(l[-1])
    
    assert(len(nmuses) == 6)
    file_pointer.close()

print(file_count)
    