memory = {}


def nb_match(code, clues):
    s = ''.join(code + list(" ".join(list(map(str, clues)))))
    if s not in memory:
        if len(code) == 0 or len(clues) == 0:
            return int(len(clues) == 0 and '#' not in code)
        elif code[0] == '.':
            return nb_match(code[1:], clues)
        elif len(code) < clues[0]:
            return 0
        elif code[0] == '?':
            if "." in code[:clues[0]] or len(code) > clues[0] and code[clues[0]] == '#':
                memory[s] = nb_match(code[1:], clues)
            else:
                memory[s] = nb_match(code[clues[0] + 1:], clues[1:]) + nb_match(code[1:], clues)
        else:
            if "." in code[:clues[0]]:
                return 0
            if len(code) > clues[0] and code[clues[0]] == '#':
                return 0
            memory[s] = nb_match(code[clues[0] + 1:], clues[1:])
    return memory[s]


t = 0
for line in open(0).read().splitlines():
    code, clues = line.split()
    code = list("?".join([code] * 5))
    clues = list(map(int, clues.split(',') * 5))
    t += nb_match(code, clues)
print(t)