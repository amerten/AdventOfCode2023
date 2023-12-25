import random
from copy import deepcopy

graph = {}
links = set()
for line in open(0).read().splitlines():
    e, r = line.split(': ')
    r = r.split()
    if e not in graph:
        graph[e] = [set(), set()]
    graph[e][0] |= set(r)
    for c in r:
        if c not in graph:
            graph[c] = [set(), set()]
        graph[c][0].add(e)
        links.add(e + "-" + c)


def lrem(l, n, v):
    if n + "-" + v in l:
        l.remove(n + "-" + v)
    elif v + "-" + n in l :
        l.remove(v + "-" + n)


def ladd(l, n, v):
    if n + "-" + v not in l and v + "-" + n not in l:
        l.add(n + "-" + v)


def merge(g, l, n, v):
    sv = g.pop(v)
    sv[0].remove(n)
    g[n][0].remove(v)
    g[n][1].add(v)
    g[n][1] |= sv[1]

    lrem(l, n, v)
    for c1 in g[n][1]:
        lrem(l, c1, v)
        for c2 in sv[1]:
            lrem(l, c1, c2)
            lrem(l, c2, n)

    g[n][0] |= sv[0]
    for c in sv[0]:
        g[c][0].add(n)
        g[c][0].remove(v)


def reduce(g, l):
    while len(g) > 2:
        u = random.choice(list(g.keys()))
        v = random.choice(list(g[u][0]))
        merge(g, l, u, v)


while True:
    g, l = deepcopy(graph), links.copy()
    reduce(g, l)
    if len(l) == 3:
        t = 1
        for k in g:
            t *= (len(g[k][0]) + len(g[k][1]))
        print(t)
        break