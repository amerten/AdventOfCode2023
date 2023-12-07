with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


time = int("".join([t for t in data[0].split() if t.isdigit()]))
distance = int("".join([d for d in data[1].split() if d.isdigit()]))

n = 0
for t in range(time):
    d = t * (time - t)
    n += d > distance
print(n)
