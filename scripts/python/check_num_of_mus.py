import os, argparse, re

parser = argparse.ArgumentParser()
parser.add_argument('-i','--i', help='input CNF file', required=True)
parser.add_argument('-alg','--alg', help='specify the name of algorithm', default="marco", required=False)

# result-${filename}.out is the output file of ${filename}
# alg-${filename}.out is the output of algorithm ${alg}
args = parser.parse_args()
number_of_mus = 0
enumeration_completed = False
output_filename = args.alg + "-" + args.i + ".out"
if args.alg == "tome" or args.alg == "remus":
    last_time_enumeration = None
    for line in open(output_filename):
        if line.strip().startswith("Found MUS"):
            number_of_mus += 1
            stat = re.split(':|,|#', line)
            # if number_of_mus % 100 == 0:
            #     print("[{0}] {1} MUS enumerated in time: {2}".format(args.alg, stat[1], float(stat[9])))
            last_time_enumeration = float(stat[9])
        elif line.strip().startswith("Enumeration completed"):
            enumeration_completed = True
        elif line.strip().startswith("Number of MUSes:"):
            number_of_mus = int(line.strip().split()[-1])

    # finally writing down the statistics
    print("The statistics of {0}".format(args.alg))
    print("The last time of enumeration: {0}".format(last_time_enumeration))
    print("=> {0} The number of MUS: {1}".format(args.alg, number_of_mus))
    print("=> {0} Complete enumeration: {1}".format(args.alg, enumeration_completed))

elif args.alg == "marco":
    enumeration_completed = True
    for line in open(output_filename):
        if line.strip().startswith("U"):
            number_of_mus += 1
        elif line.startswith("Time limit reached"):
            enumeration_completed = False

    # finally writing down the statistics
    print("The statistics of {0}".format(args.alg))
    print("=> {0} The number of MUS: {1}".format(args.alg, number_of_mus))
    print("=> {0} Complete enumeration: {1}".format(args.alg, enumeration_completed))

# compress the file
os.system("xz -f {0}".format(output_filename))
