with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def calibration_value(line):
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    v = [None, None]
    for i, c in enumerate(line):
        if c in numbers.values():
            if not v[0] and not v[1]:
                v[0] = c
            else:
                v[1] = c
        for n in numbers:
            if n in line[i:] and line.index(n, i) == i:
                if not v[0] and not v[1]:
                    v[0] = numbers[n]
                else:
                    v[1] = numbers[n]
                break
    if not v[1]:
        return int(v[0] + v[0])
    return int(v[0] + v[1])

print(sum(map(calibration_value, data)))
