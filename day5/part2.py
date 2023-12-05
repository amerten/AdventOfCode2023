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
seen = set()

for i_s in range(0, len(seeds), 2):
    s_from, s_range = seeds[i_s], seeds[i_s + 1]
    print(s_from, s_range)
    for seed in range(s_from, s_from + s_range):
        if seed in seen:
            continue
        seen.add(seed)
        i = 0
        while i < len(chain) - 1:
            source, destination = chain[i], chain[i + 1]
            for s, d, r in m[source, destination]:
                if s <= seed < (s + r):
                    seed = d + seed - s
                    break
            i += 1
        location_nb = min(location_nb, seed)

print(location_nb)

