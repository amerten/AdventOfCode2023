def next_val(sequence):
    if sequence.count(0) == len(sequence):
        return 0
    next_sequence = []
    for i in range(len(sequence) - 1):
        next_sequence.append(sequence[i+1]-sequence[i])
    return sequence[0] - next_val(next_sequence)


oasis = [list(map(int, l.split())) for l in open('input.txt').readlines()]
print(sum(map(next_val, oasis)))