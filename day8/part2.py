import re


def decomp(n):
    L = dict()
    k = 2
    while n != 1:
        exp = 0
        while n % k == 0:
            n = n // k
            exp += 1
        if exp != 0:
            L[k] = exp
        k = k + 1

    return L


def _ppcm(a, b):
    Da = decomp(a)
    Db = decomp(b)
    p = 1
    for facteur, exposant in Da.items():
        if facteur in Db:
            exp = max(exposant, Db[facteur])
        else:
            exp = exposant

        p *= facteur ** exp

    for facteur, exposant in Db.items():
        if facteur not in Da:
            p *= facteur ** exposant

    return p


def ppcm(L):
    if len(L) == 2:
        return _ppcm(L[0], L[1])
    else:
        n = len(L)
        i = 0
        A = []
        while i <= n - 2:
            A.append(_ppcm(L[i], L[i + 1]))
            i += 2

        if n % 2 != 0:
            A.append(L[n - 1])

        return ppcm(A)


with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

instructions = data[0]
maps = {}
nodes = []
for line in data[2:]:
    m = re.findall("\w{3}", line)
    maps[m[0]] = (m[1], m[2])
    if m[0][-1] == 'A' and m[0] not in nodes:
        nodes.append(m[0])
steps = []
for n in nodes:
    nb_steps = 0
    while n[-1] != 'Z':
        direction = instructions[nb_steps % len(instructions)] == "R"
        n = maps[n][direction]
        nb_steps += 1
    steps.append(nb_steps)

print(ppcm(steps))