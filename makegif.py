import sys

import oisin

filename = "input/hpbook1.txt"
nlines = 100
output = "output/generatedpoem.gif"
try:
    filename = sys.argv[1]
    nlines = int(sys.argv[2])
    output = sys.argv[3]
except IndexError:
    pass

oisin.animate(
    oisin.stepthrough(
        oisin.load(filename)[:nlines], oisin.sonnet, verbose=True), output)
