import sys

import oisin

filename = "input/hpbook1.txt"
try:
    filename = sys.argv[1]
except IndexError:
    pass

oisin.balladize(
    oisin.load(filename),
    meter=oisin.iambic(4, 'aabbccdd'),
    step=50,
    order=3)
