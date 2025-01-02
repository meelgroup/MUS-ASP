import glob, os, json, subprocess, math
import matplotlib.pyplot as plt

res_dir = "initial-9097461.pbs101" # it contains all baseline results
# res_dir = "initial-8186374.pbs101" # random benchmarks 
output_file = "output/" + res_dir + ".out"
summary_file = "output/summary_" + res_dir + ".out"
dir_name = res_dir + "/" + "result-*"
os.system('mkdir -p output')
out_file = open(output_file, 'w')
summ_file = open(summary_file, 'w')
import xlsxwriter
workbook = xlsxwriter.Workbook('MUS-ASP_count.xlsx')
worksheet = workbook.add_worksheet("result")

worksheet.write(0, 0, "Name")
worksheet.write(0, 1, "|clause|")
worksheet.write(0, 2, "MUS-ASP C.")
worksheet.write(0, 3, "MUS-ASP T.")
worksheet.write(0, 4, "CountMUST C.")
worksheet.write(0, 5, "CountMUST T.")

total_num_files = 0
total_clingo_time = 0
total_countmust_time = 0

total_clingo_timeout = 0
total_countmust_timeout = 0

total_clingo_enumerated = 0
total_countmust_enumerated = 0
mus_counted = 0

experiment_timeout = 3600
par = 2

output_mismatch = 0
output_checked = 0

clingo_mus_time_list = []
countmust_mus_time_list = []

clingo_solver = {
    "stats": {
    },
    "preamble": {
        "benchmark": "my-benchmark-set",
        "prog_args": "-a hello --arg2 world -v",
        "program": "MUS-ASP",
        "prog_alias": "MUS-ASP"
    }
}

countmust_solver = {
    "stats": {
    },
    "preamble": {
        "benchmark": "my-benchmark-set",
        "prog_args": "-a hello --arg2 world -v",
        "program": "CountMUST",
        "prog_alias": "CountMUST"
    }
}

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
    clingo_timeout = True

    countmust_count = None
    countmust_time = None
    clingo_preprocessing_time = None
    size = None
    
    total_num_files += 1
    for line in f:
        if line.startswith("CPU Time"):
            l = line.split()
            clingo_time = float(l[-1].replace("s", ""))
        elif line.startswith("Models"):
            l = line.split()
            if "+" in line:
                clingo_count = int(l[-1].replace("+", ""))
            else:
                clingo_count = int(l[-1])
                clingo_timeout = False
        elif line.startswith("MUS count:"):
            l = line.split()
            countmust_count = int(l[-1])
        elif line.startswith("Total execution (clock) time in seconds:"):
            if countmust_time == None:
                l = line.split()
                countmust_time = float(l[-1])
            else:
                l = line.split()
                clingo_preprocessing_time = float(l[-1])
        elif line.startswith("autarky size"): 
            l = line.split()
            size = int(l[-2])
            

    if clingo_timeout == True:
        total_clingo_timeout += 1
        total_clingo_time += par * experiment_timeout 
        clingo_solver["stats"]["{0}".format(total_num_files)] = {
            "status": 0,
            "rtime": experiment_timeout
        }
    else:
        total_clingo_time += (clingo_time + clingo_preprocessing_time)
        clingo_solver["stats"]["{0}".format(total_num_files)] = {
            "status": 1,
            "rtime": clingo_time + clingo_preprocessing_time
        }
    if countmust_count == -1:
        total_countmust_timeout += 1
        total_countmust_time += par * experiment_timeout
        countmust_solver["stats"]["{0}".format(total_num_files)] = {
            "status": 0,
            "rtime": experiment_timeout
        }
    else:
        total_countmust_time += countmust_time
        countmust_solver["stats"]["{0}".format(total_num_files)] = {
            "status": 1,
            "rtime": countmust_time
        }

    if clingo_timeout == False and countmust_count > -1:
        assert(clingo_count == countmust_count)
        clingo_mus_time_list.append(clingo_time + clingo_preprocessing_time)
        countmust_mus_time_list.append(countmust_time)
        output_checked += 1

    # checking whether any instance solved by countmust, but not by clingo
    # if clingo_timeout == False and countmust_count == -1:
    #     print(file)

    worksheet.write(total_num_files, 0, os.path.basename(file))
    worksheet.write(total_num_files, 1, size)
    if clingo_timeout == True:
        worksheet.write(total_num_files, 2, "NA")
        worksheet.write(total_num_files, 3, "NA")
    else:
        worksheet.write(total_num_files, 2, clingo_count)
        worksheet.write(total_num_files, 3, clingo_time)
    if countmust_count == -1:
        worksheet.write(total_num_files, 4, "NA")
        worksheet.write(total_num_files, 5, "NA")
    else:
        worksheet.write(total_num_files, 4, countmust_count)
        worksheet.write(total_num_files, 5, countmust_time)

        

print("Number of input checked: {0}".format(output_checked))
print("Clingo timeout: {0} ({1}) countmust timeout: {2} ({3})".format(total_clingo_timeout, total_num_files - total_clingo_timeout, total_countmust_timeout, total_num_files - total_countmust_timeout))
print("Clingo PAR-2: {0} countmust PAR-2: {1}".format(total_clingo_time/total_num_files, total_countmust_time/total_num_files))


workbook.close()
# plt.scatter(clingo_mus_time_list, countmust_mus_time_list, marker='x', s = 40)

# xlimit = 3600
# ylimit = 3600
# plt.xlabel("MUS-ASP")
# plt.ylabel("CountMUST")
# plt.xlim([0, xlimit])
# plt.ylim([0, ylimit])
# x1, y1 = [0, 3600], [0, 3600]
# plt.plot(x1, y1, color = 'green')
# plt.savefig("solution/{0}.pdf".format("count_mus"), format="pdf")
# plt.clf()

with open('solver1.json', 'w') as f:
    json.dump(clingo_solver, f, indent=4)
with open('solver2.json', 'w') as f:
    json.dump(countmust_solver, f, indent=4)
    

    