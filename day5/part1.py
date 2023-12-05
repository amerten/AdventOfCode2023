import sys

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

seeds = list(map(int, data[0].split(': ')[1].split()))

m = {}

chain = ["seed"]
for line in data[2:]:
    if "-to-" in line:
        source = line.split()[0].split('-to-')[0]
        destination = line.split()[0].split('-to-')[1]
        chain.append(destination)
    elif len(line) > 0:
        d, s, r = map(int, line.split())
        if (source, destination) not in m:
            m[source, destination] = []
        m[source, destination].append((int(s), int(d), int(r)))

location_nb = sys.maxsize

for seed in seeds:
    i = 0
    vals = [seed]
    while i < len(chain) - 1:
        source, destination = chain[i], chain[i + 1]
        for s, d, r in m[source, destination]:
            if s <= seed < (s + r):
                seed = d + seed - s
                break
        vals.append(seed)
        i += 1
    location_nb = min(location_nb, seed)

print(location_nb)

