import matplotlib.pyplot as plt
import numpy as np
import json

output = json.load(open("output_mus.json"))
plt.rcParams["figure.figsize"] = [4, 4]
plt.rcParams["figure.autolayout"] = True

marco_count = [_[1] if _[1] != 0 else 1 for _ in output['marco']]
remus_count = [_[1] if _[1] != 0 else 1 for _ in output['remus']]
tome_count = [_[1] if _[1] != 0 else 1 for _ in output['unimus']]
mus_asp_count = [_[0] if _[0] != 0 else 1 for _ in output['marco']]

plt.scatter(marco_count, mus_asp_count, marker='x', s = 40)

xlimit = max(max(mus_asp_count), max(marco_count)) + 50
ylimit = max(max(mus_asp_count), max(marco_count)) + 50
start = 1
plt.xlabel("MARCO")
plt.ylabel("MUS-ASP")
plt.semilogx()
plt.semilogy()
plt.xlim([start, xlimit])
plt.ylim([start, ylimit])
x1, y1 = [start, max(xlimit, ylimit)], [start, max(xlimit, ylimit)]
plt.plot(x1, y1, color = 'green')
plt.savefig("solution/{0}.pdf".format("marco"), format="pdf")
plt.clf()

plt.scatter(remus_count, mus_asp_count, marker='x', s = 40)

xlimit = max(max(mus_asp_count), max(remus_count)) + 50
ylimit = max(max(mus_asp_count), max(remus_count)) + 50
plt.xlabel("ReMUS")
plt.ylabel("MUS-ASP")
plt.semilogx()
plt.semilogy()
plt.xlim([start,xlimit])
plt.ylim([start,ylimit])
x1, y1 = [start, max(xlimit, ylimit)], [start, max(xlimit, ylimit) + 50]
plt.plot(x1, y1, color = 'green')
plt.savefig("solution/{0}.pdf".format("remus"), format="pdf")
plt.clf()

plt.scatter(tome_count, mus_asp_count, marker='x', s = 40)

xlimit = max(max(mus_asp_count), max(tome_count)) + 50
ylimit = max(max(mus_asp_count), max(tome_count)) + 50
plt.xlabel("TOME")
plt.ylabel("MUS-ASP")
plt.semilogx()
plt.semilogy()
plt.xlim([start, xlimit])
plt.ylim([start, ylimit])
x1, y1 = [start, max(xlimit, ylimit)], [start, max(xlimit, ylimit)]
plt.plot(x1, y1, color = 'green')
plt.savefig("solution/{0}.pdf".format("tome"), format="pdf")
plt.clf()

marco_better = 0
mus_better = 0
marco_succeed = 0 
fold = 1

for _ in output['marco']:
    if _[0] == 0 and _[1] > 0:
        marco_succeed += 1
        marco_better += 1
    elif _[0] > fold * _[1]:
        mus_better += 1
    elif _[0] < _[1]:
        marco_better += 1

print("MARCO", marco_succeed, mus_better, marco_better)

marco_better = 0
mus_better = 0
marco_succeed = 0 

for _ in output['remus']:
    if _[0] == 0 and _[1] > 0:
        marco_succeed += 1
        marco_better += 1
    elif _[0] > fold * _[1]:
        mus_better += 1
    elif _[0] < _[1]:
        marco_better += 1

print("ReMUS", marco_succeed, mus_better, marco_better)

marco_better = 0
mus_better = 0
marco_succeed = 0 

for _ in output['unimus']:
    if _[0] == 0 and _[1] > 0:
        marco_succeed += 1
        marco_better += 1
    elif _[0] > fold * _[1]:
        mus_better += 1
    elif _[0] < _[1]:
        marco_better += 1

print("UNIMUS", marco_succeed, mus_better, marco_better)
