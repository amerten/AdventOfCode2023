def my_hash(s):
    t = 0
    for c in s:
        t += ord(c)
        t *= 17
        t %= 256
    return t


print(sum(map(my_hash, open(0).read().replace('\n', '').split(','))))