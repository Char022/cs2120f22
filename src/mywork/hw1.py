# Charlie Alhusen - scq3ss
from z3 import *
from itertools import combinations

def atMostOne(literals):
    c = []
    for pair in combinations(literals, 2):
        a, b = pair[0], pair[1]
        c += [Or(Not(a)), Not(b)]
    return And(c)

x = [[Bool("x_%i_%i" % (i, j)) for j in range(5)] for i in range(5)]

s = Solver()

for i in range(5):
    s.add(Or(x[i]))
    
for i in range(5):
    col = []
    for j in range(5):
        col += [x[j][i]]
    s.add(atMostOne(col))
    s.add(atMostOne(x[i]))

for i in range(4):
    diag_1 = []
    diag_2 = []
    diag_3 = []
    diag_4 = []
    for j in range(5-i):
        diag_1 += [x[i+j][j]]
        diag_2 += [x[i+j][4-j]]
        diag_3 += [x[4-(i+j)][j]]
        diag_4 += [x[4-(i+j)][4-j]]
    
    s.add(atMostOne(diag_1))
    s.add(atMostOne(diag_2))
    s.add(atMostOne(diag_3))
    s.add(atMostOne(diag_4))

print(s.check())

m = s.model()

for i in range(5):
    line = ""
    for j in range(5):
        if m.evaluate(x[i][j]):
            line += "x "
        else:
            line += ". "
    print(line) 

