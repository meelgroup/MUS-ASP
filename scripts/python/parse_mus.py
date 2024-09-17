import glob, os, json, subprocess, math

res_dir = "initial-8120825.pbs101" # it contains all baseline results
# res_dir = "initial-8186374.pbs101" # random benchmarks 
output_file = "output/" + res_dir + ".out"
summary_file = "output/summary_" + res_dir + ".out"
dir_name = res_dir + "/" + "result-*"
os.system('mkdir -p output')
out_file = open(output_file, 'w')
summ_file = open(summary_file, 'w')
import xlsxwriter
workbook = xlsxwriter.Workbook('MUS-ASP.xlsx')
worksheet = workbook.add_worksheet("result")

worksheet.write(0, 0, "Name")
worksheet.write(0, 1, "|clause|")
worksheet.write(0, 2, "MUS-ASP C.")
worksheet.write(0, 3, "MUS-ASP T.")
worksheet.write(0, 4, "ReMUS C.")
worksheet.write(0, 5, "ReMUS T.")
worksheet.write(0, 6, "MARCO C.")
worksheet.write(0, 7, "MARCO T.")
worksheet.write(0, 8, "TOME C.")
worksheet.write(0, 9, "TOME T.")

total_num_files = 0
total_clingo_time = 0
total_clingo_p_time = 0
total_marco_time = 0
total_tome_time = 0
total_remus_time = 0

total_clingo_timeout = 0
total_clingo_p_timeout = 0
total_marco_timeout = 0
total_tome_timeout = 0
total_remus_timeout = 0

total_clingo_enumerated = 0
total_clingo_p_enumerated = 0
total_marco_enumerated = 0
total_tome_enumerated = 0
total_remus_enumerated = 0

tol = list()
tap_list = [0,0,0,0,0]
hybrid_tap_list = [0,0,0,0,0]
clingo_index = 0
marco_index = 1
remus_index = 2
tome_index = 3
mus_asp_index = 4
redundant = 0
experiment_timeout = 3600
par = 2
clause_thresh = 2500

output_mismatch = 0
output_checked = 0

clingo_mus_count_list = []
clingo_p_mus_count_list = []
marco_mus_count_list = []
tome_mus_count_list = []
remus_mus_count_list = []

compare_remus = []
compare_tome = []
compare_marco = []
compare_hybrid_remus = []
compare_hybrid_tome = []
compare_hybrid_marco = []

# length_json = dict()
num_of_soft_constraints = json.load(open("length.json"))

# if want to compare Wasp as well
# wasp_result = "initial-8186875.pbs101.json"
# factors = open(wasp_result) # the cyclic result is herewith
# factor_result = json.load(factors)
# def parse_wasp_result(file):
#     key = file
#     if key in factor_result:
#         return factor_result[key]
#     return {}


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

def number_of_constraint(file):
    xz_file = file.replace("result", "tome") 
    # if "random_instance" in file:
    #     length_json[os.path.basename(file)] = 1
    #     return 1
    # os.system('unxz {0}'.format(xz_file + ".xz"))
    # sc_size = subprocess.Popen('grep "Number of constraints in the input set:" {0}'.format(xz_file), shell=True, stdout=subprocess.PIPE).stdout
    # sc_size =  sc_size.read().decode("utf-8").strip().split(":")
    # num_of_soft_clauses = int(sc_size[-1])
    # # again zip it
    # os.system('xz {0}'.format(xz_file))
    # # write down the ncls
    # length_json[os.path.basename(file)] = num_of_soft_clauses
    num_of_soft_clauses = num_of_soft_constraints[os.path.basename(file)]
    return num_of_soft_clauses

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

    tome_count = None
    tome_time = None
    tome_solution = False
    tome_timeout = False

    remus_count = None
    remus_time = None
    remus_solution = False
    remus_timeout = False

    unprocessed = True
    nmuses = [None] * 5
    ntimes = [0] * 5
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
                
                unprocessed = False
                nmuses[clingo_index] = clingo_count
            else:
                if "+" in line:
                    clingo_p_count = int(l[-1].replace("+", ""))
                else:
                    clingo_p_count = int(l[-1])
                    clingo_p_timeout = False
                
                nmuses[mus_asp_index] = clingo_p_count
        elif line.startswith("Total execution (clock) time in seconds"):
            l = line.split()
            clingo_preprocessing_time = float(l[-1])
        elif line.startswith("=> tome Complete enumeration: False"):
            tome_timeout = True
        elif line.startswith("=> marco Complete enumeration: False"):
            marco_timeout = True
        elif line.startswith("=> remus Complete enumeration: False"):
            remus_timeout = True
        elif line.startswith("=> tome The number of MUS:"):
            l = line.split()
            tome_count = int(l[-1])
            
            nmuses[tome_index] = tome_count
        elif line.startswith("=> marco The number of MUS:"):
            l = line.split()
            marco_count = int(l[-1])
            
            nmuses[marco_index] = marco_count
        elif line.startswith("=> remus The number of MUS:"):
            l = line.split()
            remus_count = int(l[-1])
            
            nmuses[remus_index] = remus_count


    clingo_p_time = get_time(file, "mus") + clingo_preprocessing_time
    ntimes[mus_asp_index] = clingo_p_time
    clingo_time = get_time(file, "clingo")
    ntimes[clingo_index] = clingo_time
    tome_time = get_time(file, "tome")
    ntimes[tome_index] = tome_time
    marco_time = get_time(file, "marco")
    ntimes[marco_index] = marco_time
    remus_time = get_time(file, "remus")
    ntimes[remus_index] = remus_time
    true_mus_count = None
    if marco_timeout == False:
        assert(marco_count != None)
        true_mus_count = marco_count 
    if true_mus_count != None and clingo_timeout == False:
        if true_mus_count != clingo_count:
            print("[Output mismatch]: {0}".format(file))
            output_mismatch += 1
        output_checked += 1

    if total_num_files % 100 == 0:
        print("{0} files processed".format(total_num_files))
    
    if None not in nmuses and 0 not in nmuses and len(set(nmuses)) == 1:
        # print(file, nmuses)
        redundant += 1
        continue
    
    remus_mus_count_list.append(log_value(remus_count))
    marco_mus_count_list.append(log_value(marco_count))
    tome_mus_count_list.append(log_value(tome_count))
    clingo_p_mus_count_list.append(log_value(clingo_count))
    clingo_mus_count_list.append(log_value(clingo_count))
    # if want to compare Wasp
    # wasp_mus_result = parse_wasp_result(os.path.basename(file))
    # if wasp_mus_result != {}:
    #     nmuses[clingo_index] = wasp_mus_result["count"]
    #     ntimes[clingo_index] = wasp_mus_result["time"]
    # else:
    #     nmuses[clingo_index] = 0
    #     ntimes[clingo_index] = 3600

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
    if tome_timeout == False:
        total_tome_enumerated += 1
        total_tome_time += tome_time
    else:
        total_tome_time += par * experiment_timeout
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

    nclauses = number_of_constraint(file)
    min_count = None
    for _ in nmuses:
        if min_count == None or min_count > _:
            min_count = _ 
    for index, _ in enumerate(nmuses):
        if nmuses[index] == 0:
            tap_list[index] += par * experiment_timeout
        else:
            tap_list[index] += ntimes[index] + experiment_timeout * (1 + math.log2(min_count + 1)) / (1 + math.log2(nmuses[index] + 1)) 
        
        ref_index = index
        if nclauses < clause_thresh:
            ref_index = 4
        if nmuses[ref_index] == 0:
            hybrid_tap_list[index] += par * experiment_timeout
        else:
            hybrid_tap_list[index] += ntimes[ref_index] + experiment_timeout * (1 + math.log2(min_count + 1)) / (1 + math.log2(nmuses[ref_index] + 1)) 

    compare_remus.append((clingo_p_count,remus_count))
    compare_tome.append((clingo_p_count,tome_count))
    compare_marco.append((clingo_p_count,marco_count))
    if nclauses < clause_thresh:
        compare_hybrid_remus.append((clingo_p_count,remus_count))
        compare_hybrid_tome.append((clingo_p_count,tome_count))
        compare_hybrid_marco.append((clingo_p_count,marco_count))
    else:
        compare_hybrid_remus.append((remus_count,remus_count))
        compare_hybrid_tome.append((tome_count,tome_count))
        compare_hybrid_marco.append((marco_count,marco_count))
    
    worksheet.write(total_num_files - redundant, 0, os.path.basename(file))
    worksheet.write(total_num_files - redundant, 1, nclauses)
    worksheet.write(total_num_files - redundant, 2, clingo_p_count)
    worksheet.write(total_num_files - redundant, 3, clingo_p_time)
    worksheet.write(total_num_files - redundant, 4, remus_count)
    worksheet.write(total_num_files - redundant, 5, remus_time)
    worksheet.write(total_num_files - redundant, 6, marco_count)
    worksheet.write(total_num_files - redundant, 7, marco_time)
    worksheet.write(total_num_files - redundant, 8, tome_count)
    worksheet.write(total_num_files - redundant, 9, tome_time)


print("Total number of files: {0}".format(total_num_files))
print("Output mismatched: {0}".format(output_mismatch))
print("Output checked: {0}".format(output_checked))
print("Clingo + Prep enumerated: {0}".format(total_clingo_p_enumerated))
print("Clingo enumerated: {0}".format(total_clingo_enumerated))
print("tome enumerated: {0}".format(total_tome_enumerated))
print("MARCO enumerated: {0}".format(total_marco_enumerated))
print("REMUS enumerated: {0}".format(total_remus_enumerated))
# print(sorted(clingo_mus_count_list))
# print(sorted(marco_mus_count_list))
# print(sorted(tome_mus_count_list))
# print(sorted(clingo_p_mus_count_list))
# print(sorted(remus_mus_count_list))
print("marco = ", compare_marco)
print("remus = ", compare_remus)
print("tome = ", compare_tome)
print("hybrid_marco = ", compare_hybrid_marco)
print("hybrid_remus = ", compare_hybrid_remus)
print("hybrid_tome = ", compare_hybrid_tome)
print("Clingo PAR-2 score: {0}".format(total_clingo_time/total_num_files))
print("Clingo + Prep PAR-2 score: {0}".format(total_clingo_p_time/total_num_files))
print("MARCO PAR-2 score: {0}".format(total_marco_time/total_num_files))
print("tome PAR-2 score: {0}".format(total_tome_time/total_num_files))
print("remus PAR-2 score: {0}".format(total_remus_time/total_num_files))
print([_/(total_num_files - redundant) for _ in tap_list])
print([_/(total_num_files - redundant) for _ in hybrid_tap_list]) # it is the hybrid MUS enumerator
print(total_num_files - redundant)
workbook.close()

# with open('{0}.json'.format("length"), 'w') as outfile:
#     json.dump(length_json, outfile)
    

    