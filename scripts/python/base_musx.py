from pysat.examples.optux import OptUx
from pysat.formula import CNF, WCNF

cnf = CNF(from_file='m1_marco_input_50_100_36.cnf')

wcnf = WCNF()
for clause in cnf.clauses:
    wcnf.append(clause, weight=1)

mus_count = 0
with OptUx(wcnf) as optux:
    for mus in optux.enumerate():
        # print('mus {0} has cost {1}'.format(mus, optux.cost))
        mus_count += 1

print("MUS count: {0}".format(mus_count))

