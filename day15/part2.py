import re


def my_hash(s):
    t = 0
    for c in s:
        t += ord(c)
        t *= 17
        t %= 256
    return t


boxes = {}

for lens in open(0).read().replace('\n', '').split(','):
    m = re.match('(\w+)(-|=)(\d*)', lens)
    label = m.group(1)
    box_nb = my_hash(label)
    op = m.group(2)
    if op == '=':
        focal = int(m.group(3))
        if box_nb not in boxes:
            boxes[box_nb] = [[], []]
        if label in boxes[box_nb][0]:
            boxes[box_nb][1][boxes[box_nb][0].index(label)] = focal
        else:
            boxes[box_nb][0].append(label)
            boxes[box_nb][1].append(focal)
    else:
        if box_nb in boxes and label in boxes[box_nb][0]:
            i = boxes[box_nb][0].index(label)
            boxes[box_nb][0] = boxes[box_nb][0][:i] + boxes[box_nb][0][i+1:]
            boxes[box_nb][1] = boxes[box_nb][1][:i] + boxes[box_nb][1][i+1:]

t = 0
for box in boxes:
    for i, focal in enumerate(boxes[box][1]):
        t += ((box + 1) * (i + 1) * focal)
print(t)