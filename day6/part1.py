import math

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


times = [int(t) for t in data[0].split() if t.isdigit()]
records = [int(d) for d in data[1].split() if d.isdigit()]


def nb_ways(race_time, record):
    n = 0
    for t in range(race_time):
        distance = t * (race_time - t)
        n += (distance > record)
    return n


print(math.prod(map(nb_ways, times, records)))
