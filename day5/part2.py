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

i = 0
while True:
    val = i
    for j, destination in enumerate(chain[:0:-1]):
        source = chain[len(chain) -1 - j - 1]
        for s, d, r in m[source, destination]:
            if d <= val < (d + r):
                val = s + val - d
                break
    for k in range(0, len(seeds) - 1, 2):
        if seeds[k] <= val < seeds[k] + seeds[k+1]:
            print(i)
            quit()
    i += 1
