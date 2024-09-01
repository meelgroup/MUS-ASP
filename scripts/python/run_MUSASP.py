import os, argparse, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-i','--i', help='input CNF file', required=True)
parser.add_argument('-h','--h', help='heuristics to be employed', required=False)
parser.add_argument('-p','--p', help='python path', required=False)
args = parser.parse_args()
python_dir = 'python'
clingo_dir = 'clingo'
heuristic = ''
if args.h == None:
    heuristic = args.h

if args.p == None:
    python_dir = 'python'

os.system('/usr/bin/time --verbose -o heu_${filename}.timeout {0} counter.py {1} {2} >> heuristic-{1}.out 2>&1'.format(python_dir, heuristic, args.i))

out_file = open('output_{0}.out'.format(args.i))
total_time = 3600
heuristic_time = None
for line in out_file:
    if line.startswith("Total execution (clock) time in seconds"):
        l = line.strip().split()
        heuristic_time = float(l[-1])

print('Time spent in heuristic: {0}'.format(heuristic))

out_file.close()
total_time = total_time - heuristic_time # remaining time
assert(total_time > 0)

os.system('/usr/bin/time --verbose -o mus_{0}.timeout clingo --enum-mode=domRec --heuristic=domain -n 0 -q --time-limit={1} mus_{0} >> result-{0}.out 2>&1'.format(args.i, total_time))


