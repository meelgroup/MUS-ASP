import os, glob, re

result_dir = "initial-7638521.pbs101"
file_for_compare = 0
def check_mus_by_mus(clingo_output, marco_output):
    inconsistent = len(clingo_output) != len(marco_output)
    if inconsistent == True:
        return inconsistent
    check_list = set()
    for mus in clingo_output:
        sorted_clauses = sorted(mus)
        for index, marco_mus in enumerate(marco_output):
            if index not in check_list and sorted_clauses == sorted(marco_mus):
                check_list.add(index)

    inconsistent = len(clingo_output) != len(check_list)
    return inconsistent

consistency_checked = 0
for file in glob.glob(result_dir + "/result-*"):
    file_pointer = open(file)
    mus_clauses = [] 
    for line in file_pointer:
        if line.strip().startswith("d("):
            clause_index = re.findall(r'\d+', line.strip())
            mus_clauses.append(clause_index)

    file_pointer.close()

    marco_file = file.replace("result", "marco") + ".xz"
    marco_result = file.replace("result", "marco")
    if os.path.exists(marco_file):
        os.system('unxz {0}'.format(marco_file))
    elif not os.path.exists(marco_result):
        assert(False)

    marco_result = file.replace("result", "marco")
    marco_pointer = open(marco_result)
    marco_mus = []
    for line in marco_pointer:
        if line.strip().startswith("U "):
            clause_index = re.findall(r'\d+', line.strip())
            marco_mus.append(clause_index)

    marco_pointer.close()
    os.system('xz {0}'.format(marco_result))
    print("Running input: {0}, MUS Count: {1}/{2}".format(os.path.basename(file), len(mus_clauses), len(marco_mus)))
    consistency_checked += 1
    inc = check_mus_by_mus(mus_clauses, marco_mus)
    if inc:
        print("INCONS: {0} {1}".format(file, marco_file))
        assert(False)

print(consistency_checked)