import glob, os, subprocess, json
# "initial-9277024.wlm01"  for small benchmarks
# "initial-8961066.wlm01"  for large benchmarks
dir_name = "initial-8186875.pbs101"
count = 0
result_json = dict()

def get_time(file, solver):
    file_name = os.path.basename(file)
    output_file = dir_name + "/" + solver + "_" + file_name[len("result-"):-len(".out")] + ".timeout"
    time = subprocess.Popen('grep "User time (seconds)" {0}'.format(output_file), shell=True, stdout=subprocess.PIPE).stdout
    time =  time.read().decode("utf-8").strip().split()
    user_time = float(time[-1])

    time = subprocess.Popen('grep "System time (seconds)" {0}'.format(output_file), shell=True, stdout=subprocess.PIPE).stdout
    time =  time.read().decode("utf-8").strip().split()
    system_time = float(time[-1])
    return user_time + system_time

for file in glob.glob(dir_name + "/result-*"):
    result_file = open(file)

    nmuses = None
    time = None
    for line in result_file:
        if line.startswith("Number of printed answers:"):
            nmuses = int(line.split()[-1])

    if nmuses != None:
        time = get_time(file, "core_prep")

        result_json[os.path.basename(file)] = {}
        result_json[os.path.basename(file)]["time"] = round(time, 3)
        result_json[os.path.basename(file)]["count"] = nmuses

with open('{0}.json'.format(dir_name), 'w') as outfile:
    json.dump(result_json, outfile)