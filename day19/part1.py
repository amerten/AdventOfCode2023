w, r = open(0).read().split('\n\n')
workflows, ratings = {}, []

for workflow in w.splitlines():
    name, rest = workflow.split('{')
    workflows[name] = rest[:-1].split(',')

for rating in r.splitlines():
    x, m, a, s = map(lambda x: int(x.split('=')[1]), rating[1:-1].split(','))
    ratings.append({'x': x, 'm': m, 'a': a, 's': s})

t = 0
for rating in ratings:
    wf = workflows['in']
    done = False
    while not done:
        for i, rule in enumerate(wf):
            if rule == 'A':
                t += sum(rating.values())
                done = True
                break
            elif rule == 'R':
                done = True
                break
            elif '<' in rule:
                comp, target = rule.split(':')
                part, n = comp.split('<')[0], int(comp.split('<')[1])
                if rating[part] < n:
                    if target == 'A':
                        t += sum(rating.values())
                        done = True
                        break
                    elif target == 'R':
                        done = True
                        break
                    else:
                        wf = workflows[target]
                        break
            elif '>' in rule:
                comp, target = rule.split(':')
                part, n = comp.split('>')[0], int(comp.split('>')[1])
                if rating[part] > n:
                    if target == 'A':
                        t += sum(rating.values())
                        done = True
                        break
                    elif target == 'R':
                        done = True
                        break
                    else:
                        wf = workflows[target]
                        break
            else:
                wf = workflows[rule]
print(t)
