space = [list(line.strip()) for line in open(0).read().splitlines()]

no_gal_lines = [i for i, line in enumerate(space) if all(n == '.' for n in line)]
no_gal_columns = [c for c, col in enumerate(zip(*space)) if all(ch == "." for ch in col)]

galaxies = [(r, c) for r in range(len(space)) for c in range(len(space[r])) if space[r][c] == '#']

t = 0
for i_g1 in range(len(galaxies) - 1):
    for i_g2 in range(i_g1 + 1, len(galaxies)):
        g1, g2 = galaxies[i_g1], galaxies[i_g2]
        d = 0
        d += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        for i in no_gal_lines:
            d += (g1[0] < i < g2[0] or g2[0] < i < g1[0])
        for i in no_gal_columns:
            d += (g1[1] < i < g2[1] or g2[1] < i < g1[1])
        t += d
print(t)