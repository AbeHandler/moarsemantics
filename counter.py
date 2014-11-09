import numpy as np
import sys
import re
import math
import numpy as np

increments = np.linspace(0, 1, num=1000)

def isIt(s, p):
    if len(re.findall(p, s)) > 0:
        return True
    return False

def lessThanTheshold(l, threshold):
    try:
        valu = float(l.split(",")[4])
        if (valu < threshold):
            return True
        return False
    except IndexError:
        return False
    except ValueError:
        return False

for i in increments:
    syn = 0
    mero = 0
    holo = 0
    hyper = 0
    hypo = 0
    stem = 0
    with open("textfiles/results.txt") as results:
        for line in results.readlines():
            line = line.replace("\n", "")
            if lessThanTheshold(line, i):
                if isIt(line, "^syn"):
                    syn += 1
                if isIt(line, "^mero"):
                    mero += 1
                if isIt(line, "^holo"):
                    holo += 1
                if isIt(line, "^hyper"):
                    hyper += 1
                if isIt(line, "^hypo"):
                    hypo += 1
                if isIt(line, "^same stem"):
                    stem += 1
    print ",".join([str(i), str(syn), str(mero), str(holo), str(hyper), str(hypo), str(stem)])

def lessThanGreaterThanK(l, k):
    try:
        ceil = float(k)
        valu = float(l.split(",")[4])
        floork = float(floor[k])
        if (valu <= k and valu > floork):
            return True
        return False
    except IndexError:
        print line
    except ValueError:
        pass