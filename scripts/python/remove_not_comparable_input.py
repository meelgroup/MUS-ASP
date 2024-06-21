import os, glob

result_dir = "initial-7638521.pbs101"
file_for_compare = 0
for file in glob.glob(result_dir + "/*.out"):
    result = os.popen('grep "Models" {0}'.format(file)).read()
    if "+" in result:
        # cannot compare
        file_for_compare += 1
        os.remove(file)
        marco_file = file.replace("result", "marco") + ".xz"
        os.remove(marco_file)

print(file_for_compare)