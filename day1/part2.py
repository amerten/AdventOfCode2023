with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def real_value(val):
    conversion = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    if val in conversion:
        return conversion[val]
    if val[::-1] in conversion:
        return conversion[val[::-1]]
    return val


def find_first(line, reverse=False):
    if reverse:
        line = line[::-1]
    for i, c in enumerate(line):
        for n in numbers:
            if reverse:
                n = n[::-1]
            if n == c or (n in line and line.index(n) == i):
                return real_value(n)


def calibration_value(line):
    return int(find_first(line) + find_first(line, True))


print(sum(map(calibration_value, data)))
