import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--i', help='input CNF file', required=True)
args = parser.parse_args()

def compute_mus_format(file_name):
    output_file = "clingo_" + file_name 
    # os.system("mv {0} {1}".format("prep_" + file_name, file_name))
    # file_pointer = open(file_name, 'r')
    file_pointer = open(file_name, 'r')
    nvar = None
    ncls = None
    cur_cls = 1
    output_file_pointer = open(output_file, 'w')
    clause_list = []
    var_list = []
    for line in file_pointer:
        if line.startswith("c"):
            continue
        elif line.startswith("p cnf"):
            l = line.split()
            nvar = int(l[-2])
            ncls = int(l[-1])
            # print("The number of literals: {0} and clauses: {1} [Unpreprocessed]".format(l[-2], l[-1]))
        else:
            l = line.split()
            rule_str = "unsat :- d({0})".format(cur_cls)
            clause_list.append(cur_cls)
            cur_cls += 1
            for index, _ in enumerate(l):
                if int(_) == 0:
                    continue
                elif int(_) > 0:
                    rule_str += (", f({0})".format(int(_)))
                elif int(_) < 0:
                    rule_str += (", t({0})".format(abs(int(_))))
                var_list.append(abs(int(_)))

            rule_str += "."
            output_file_pointer.write(rule_str + "\n")

    rule_str = ":- not unsat."
    output_file_pointer.write(rule_str + "\n")

    for var in var_list:
        rule_str = "t({0}); f({0}).".format(var)
        output_file_pointer.write(rule_str + "\n")

        rule_str = "t({0}) :- unsat.".format(var)
        output_file_pointer.write(rule_str + "\n")

        rule_str = "f({0}) :- unsat.".format(var)
        output_file_pointer.write(rule_str + "\n")

    rule_str = ""
    for index, _ in enumerate(clause_list):
        if index == 0:
            rule_str += " d({0})".format(_)
        else:
            rule_str += " ; d({0})".format(_)

    output_file_pointer.write("{" + rule_str + " }.\n")

    output_file_pointer.write("#heuristic d(X). [1, false]" + "\n")
    output_file_pointer.write("#show d/1.\n")
    file_pointer.close()
    output_file_pointer.close()

file_name = args.i
compute_mus_format(file_name)