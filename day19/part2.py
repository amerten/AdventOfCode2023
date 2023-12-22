import re


def opposite(r):
    r = r.split(':')[0]
    s = '<' if '<' in r else '>'
    os = '<' if s == '>' else '>'
    return r.split(s)[0] + os + "=" + r.split(s)[1]


w, _ = open(0).read().split('\n\n')
workflows = {}

for workflow in w.splitlines():
    name, rest = workflow.split('{')
    workflows[name] = rest[:-1].split(',')

ok_ranges = []


def update_ranges(wf_name, ok_r):
    rules = workflows[wf_name]
    for i, rule in enumerate(rules):
        previous_rules = ""
        for r in rules[:i]:
            previous_rules += opposite(r)
        if rule == 'A':
            ok_ranges.append(ok_r + previous_rules)
        elif '<' in rule or '>' in rule:
            dr, destination = rule.split(':')
            if destination == 'A':
                ok_ranges.append(ok_r + previous_rules + dr)
            elif destination != 'R':
                update_ranges(destination, ok_r + previous_rules + dr)
        elif rule != 'R':
            update_ranges(rule, ok_r + previous_rules)


update_ranges('in', "")
parts = ['x', 'm', 'a', 's']

t = 0
for ok_range in ok_ranges:
    all_ranges = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    p = "(x|m|a|s)([<>]=?)(\d+)"
    m = re.findall(p, ok_range)
    for part, sign, val in m:
        i = parts.index(part)
        if sign == '<':
            all_ranges[i][1] = min(all_ranges[i][1], int(val) - 1)
        elif sign == '<=':
            all_ranges[i][1] = min(all_ranges[i][1], int(val))
        elif sign == '>':
            all_ranges[i][0] = max(all_ranges[i][0], int(val) + 1)
        elif sign == '>=':
            all_ranges[i][0] = max(all_ranges[i][0], int(val))
        else:
            raise Exception("oops")
    sub_t = 1
    for i in range(len(all_ranges)):
        sub_t *= (all_ranges[i][1] - all_ranges[i][0] + 1)
    t += sub_t
print(t)