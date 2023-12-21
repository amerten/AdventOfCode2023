points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

p = 0
for line in open(0):
    _, _, x = line.split()
    x = x[2:-1]
    dr, dc = dirs["RDLU"[int(x[-1])]]
    n = int(x[:-1], 16)
    p += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

A = abs((sum(points[i][0] * points[i + 1][1] - points[i][1] * points[i + 1][0] for i in range(len(points) - 1))) // 2)
print(A + p // 2 + 1)
