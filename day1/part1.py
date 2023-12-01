with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def calibration_value(line):
    v = ""
    for c in line:
        if c.isdigit():
            v += c
            break
    for c in line[::-1]:
        if c.isdigit():
            v += c
            break
    return int(v)


print(sum(map(calibration_value, data)))
