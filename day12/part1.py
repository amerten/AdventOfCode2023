import itertools
import re

data = open(0).read().splitlines()


def can_match(code, clues):
    m = re.findall('#+', code)
    return len(m) == len(clues) and all(len(m[i]) == clues[i] for i in range(len(clues)))


def nb_arrangements(line):
    code, clues = line.split()
    clues = list(map(int, clues.split(",")))
    nb_unknown = code.count('?')
    nb_arrangements = 0
    for p in itertools.product('.#', repeat=nb_unknown):
        lcode = list(code)
        n = 0
        for i, c in enumerate(lcode):
            if c == '?':
                lcode[i] = p[n]
                n += 1
        nb_arrangements += can_match(''.join(lcode), clues)
    return nb_arrangements


print(sum(map(nb_arrangements, data)))