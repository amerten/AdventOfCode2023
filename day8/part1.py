import re


with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

instructions = data[0]
maps = {}
for line in data[2:]:
    m = re.findall("\w{3}", line)
    maps[m[0]] = (m[1], m[2])

nb_steps, position = 0, 'AAA'

while position != 'ZZZ':
    direction = instructions[nb_steps % len(instructions)] == "R"
    position = maps[position][direction]
    nb_steps += 1

print(nb_steps)
