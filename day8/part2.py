import re
import utils

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

print(utils.ppcm(steps))