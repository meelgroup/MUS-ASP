import glob, os, json, subprocess, math

res_dir = "initial-7774670.pbs101" # it contains all baseline results
output_file = "output/" + res_dir + ".out"
summary_file = "output/summary_" + res_dir + ".out"
dir_name = res_dir + "/" + "result-*"
os.system('mkdir -p output')
out_file = open(output_file, 'w')
summ_file = open(summary_file, 'w')

total_num_files = 0
total_clingo_time = 0
total_clingo_p_time = 0
total_marco_time = 0
total_unimus_time = 0
total_remus_time = 0

total_clingo_timeout = 0
total_clingo_p_timeout = 0
total_marco_timeout = 0
total_unimus_timeout = 0
total_remus_timeout = 0

total_clingo_enumerated = 0
total_clingo_p_enumerated = 0
total_marco_enumerated = 0
total_unimus_enumerated = 0
total_remus_enumerated = 0

tol = list()
tap_list = [0,0,0,0]
experiment_timeout = 3600
par = 2

output_mismatch = 0
output_checked = 0

clingo_mus_count_list = []
clingo_p_mus_count_list = []
marco_mus_count_list = []
unimus_mus_count_list = []
remus_mus_count_list = []

def get_time(file, solver):
    file_name = os.path.basename(file)
    output_file = res_dir + "/" + solver + "_" + file_name[len("result-"):-len(".out")] + ".timeout"
    time = subprocess.Popen('grep "User time (seconds)" {0}'.format(output_file), shell=True, stdout=subprocess.PIPE).stdout
    time =  time.read().decode("utf-8").strip().split()
    user_time = float(time[-1])

    time = subprocess.Popen('grep "System time (seconds)" {0}'.format(output_file), shell=True, stdout=subprocess.PIPE).stdout
    time =  time.read().decode("utf-8").strip().split()
    system_time = float(time[-1])
    return user_time + system_time


def log_value(n: int):
    return round(math.log10(n), 2) if n > 0 else 0
for file in glob.glob(dir_name):
    f = open(file, 'r')
    out_file.write("File: " + file + "\n")

    clingo_count = None
    clingo_time = None
    clingo_solution = False
    clingo_timeout = True
    clingo_p_count = None
    clingo_p_time = None
    clingo_p_solution = False
    clingo_p_timeout = True
    clingo_preprocessing_time = None

    marco_count = None
    marco_time = None
    marco_solution = False
    marco_timeout = False

    unimus_count = None
    unimus_time = None
    unimus_solution = False
    unimus_timeout = False

    remus_count = None
    remus_time = None
    remus_solution = False
    remus_timeout = False

    unprocessed = True

    total_num_files += 1
    for line in f:
        if line.startswith("CPU Time"):
            l = line.split()
            clingo_time = float(l[-1].replace("s", ""))
        elif line.startswith("Models"):
            l = line.split()
            if unprocessed:
                if "+" in line:
                    clingo_count = int(l[-1].replace("+", ""))
                else:
                    clingo_count = int(l[-1])
                    clingo_timeout = False
                clingo_mus_count_list.append(log_value(clingo_count))
                unprocessed = False
            else:
                if "+" in line:
                    clingo_p_count = int(l[-1].replace("+", ""))
                else:
                    clingo_p_count = int(l[-1])
                    clingo_p_timeout = False
                clingo_p_mus_count_list.append(log_value(clingo_count))
        elif line.startswith("Total execution (clock) time in seconds"):
            l = line.split()
            clingo_preprocessing_time = float(l[-1])
        elif line.startswith("=> unimus Complete enumeration: False"):
            unimus_timeout = True
        elif line.startswith("=> marco Complete enumeration: False"):
            marco_timeout = True
        elif line.startswith("=> remus Complete enumeration: False"):
            remus_timeout = True
        elif line.startswith("=> unimus The number of MUS:"):
            l = line.split()
            unimus_count = int(l[-1])
            unimus_mus_count_list.append(log_value(unimus_count))
        elif line.startswith("=> marco The number of MUS:"):
            l = line.split()
            marco_count = int(l[-1])
            marco_mus_count_list.append(log_value(marco_count))
        elif line.startswith("=> remus The number of MUS:"):
            l = line.split()
            remus_count = int(l[-1])
            remus_mus_count_list.append(log_value(remus_count))


    clingo_p_time = get_time(file, "mus") + clingo_preprocessing_time
    clingo_time = get_time(file, "clingo")
    unimus_time = get_time(file, "unimus")
    marco_time = get_time(file, "marco")
    remus_time = get_time(file, "remus")
    true_mus_count = None
    if unimus_timeout == False or marco_timeout == False:
        assert(unimus_count != None or marco_count != None)
        true_mus_count = unimus_count if unimus_count != None else marco_count 
    if true_mus_count != None and clingo_timeout == False:
        if true_mus_count != clingo_count:
            print("[Output mismatch]: {0}".format(file))
            output_mismatch += 1
        output_checked += 1

    if total_num_files % 100 == 0:
        print("{0} files processed".format(total_num_files))

    if clingo_timeout == False:
        total_clingo_enumerated += 1
        total_clingo_time += clingo_time
    else:
        total_clingo_time += par * experiment_timeout
    if clingo_p_timeout == False:
        total_clingo_p_enumerated += 1
        total_clingo_p_time += clingo_p_time
    else:
        total_clingo_p_time += par * experiment_timeout
    if unimus_timeout == False:
        total_unimus_enumerated += 1
        total_unimus_time += unimus_time
    else:
        total_unimus_time += par * experiment_timeout
    if marco_timeout == False:
        total_marco_enumerated += 1
        total_marco_time += marco_time
    else:
        total_marco_time += par * experiment_timeout
    if remus_timeout == False:
        total_remus_enumerated += 1
        total_remus_time += remus_time
    else:
        total_remus_time += par * experiment_timeout

print("Total number of files: {0}".format(total_num_files))
print("Output mismatched: {0}".format(output_mismatch))
print("Output checked: {0}".format(output_checked))
print("Clingo + Prep enumerated: {0}".format(total_clingo_p_enumerated))
print("Clingo enumerated: {0}".format(total_clingo_enumerated))
print("UNIMUS enumerated: {0}".format(total_unimus_enumerated))
print("MARCO enumerated: {0}".format(total_marco_enumerated))
print("REMUS enumerated: {0}".format(total_remus_enumerated))
print(sorted(clingo_mus_count_list))
print(sorted(marco_mus_count_list))
print(sorted(unimus_mus_count_list))
print(sorted(clingo_p_mus_count_list))
print(sorted(remus_mus_count_list))
print("Clingo PAR-2 score: {0}".format(total_clingo_time/total_num_files))
print("Clingo + Prep PAR-2 score: {0}".format(total_clingo_p_time/total_num_files))
print("MARCO PAR-2 score: {0}".format(total_marco_time/total_num_files))
print("unimus PAR-2 score: {0}".format(total_unimus_time/total_num_files))
print("remus PAR-2 score: {0}".format(total_remus_time/total_num_files))
    

    