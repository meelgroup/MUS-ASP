import os
import os, glob, math

# result_dir = "initial-8101398.pbs101"
result_dir = "initial-8186062.pbs101"
file_count = 0
tap = [0] * 4
rank_list = [0] * 4
# enumerated = [0] * 4
timeout = 3600
par = 2
consistency_checked = 0
max_preproc_time = 0
for file in glob.glob(result_dir + "/result-*"):
    file_pointer = open(file)
    nmuses = []
    exact_mus = []
    ntimes = [] 
    nproc = [] 
    ground_truth = None
    file_count += 1
    for line in file_pointer:
        if line.startswith("Models"):
            l = line.split()
            if "+" not in l[-1].strip():
                # enumerated[len(nmuses)] = enumerated[len(nmuses)] + 1
                exact_mus.append(int(l[-1].replace("+", "")))
                if len(nmuses) == 0:
                    # non heuristic number of muses
                    ground_truth = int(l[-1].replace("+", ""))
            nmuses.append(int(l[-1].replace("+", "")))

        elif line.startswith("CPU Time"):
            l = line.split()
            ntimes.append(float(l[-1].replace("s", "")))
        elif line.startswith("Time spent in heuristic"):
            l = line.split()
            nproc.append(float(l[-1]))
            # max_preproc_time = max(max_preproc_time, float(l[-1]))
    # if len(nmuses) != 4:
    #     print(file)
    assert(len(nmuses) == 4)
    assert(len(ntimes) == 4)
    assert(len(nproc) == 4)

    # computing tap score, first compute min
    min_count = nmuses[0]
    for _ in nmuses:
        if _ < min_count:
            min_count = _
    
    # computing tap score, then second step of linear equation
    if min_count > 0:
        for index, _ in enumerate(nmuses):
            if nmuses[index] == 0:
                tap[index] += par * timeout
            else:
                tap[index] += ntimes[index] + timeout * (1 + math.log2(min_count)) / (1 + math.log2(nmuses[index])) 
    # it is the sanity check
    if ground_truth != None:
        for _ in nmuses:
            assert(_ == ground_truth)
    # compute rank
    rank = [sorted(l, reverse = True).index(x) + 1 for x in nmuses]
    for _, index in enumerate(rank):
        rank_list[index] += rank[index]

    # all heuristic are correct
    assert(len(set(exact_mus)) <= 1)
    file_pointer.close()

print([round(_/file_count,3) for _ in tap]) # computing average TAP score
print([round(_/file_count,3) for _ in rank_list]) # rank of each solver
# print(enumerated) # number of exact enumeration 
print(file_count)
    